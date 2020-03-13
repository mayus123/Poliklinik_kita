# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class ResPartner(models.Model):
    _inherit = "res.partner"

    pasien = fields.Boolean('Pasien ?')
    dokter = fields.Boolean('Dokter ?')
    # penerbit = fields.Boolean('Penerbit ?')
    
 
 
    tanggalpendaftaran = fields.Date('Tanggal Pendaftaran', default=date.today())
    
    # death_date = fields.Date('Date of Death')
 
    # biography = fields.Text('Biography')
    # lang = fields.Selection(string='Language', selection='_get_lang')
 
 
    # _sql_constraints = [('name_uniq', 'unique (name)', 'Nama harus unik !')]
 
    # @api.model
    # def _get_lang(self):
    #     return self.env['res.lang'].get_installed()     

    # penulis = fields.Boolean('Penulis ?')
    # anggota = fields.Boolean('Anggota ?')
    # penerbit = fields.Boolean('Penerbit ?')
 
    # born_date = fields.Date('Date of Birth')
    # death_date = fields.Date('Date of Death')
 
    # biography = fields.Text('Biography')
    # lang = fields.Selection(string='Language', selection='_get_lang')
 
 
    # _sql_constraints = [('name_uniq', 'unique (name)', 'Nama harus unik !')]
    # _rec_name = 'no'

    # Registrasi Pasien
    # no = fields.Char(string="No Antrian",default="/", readonly=True)
    # nama = fields.Many2one('res.partner', string="Nama", required=True)
    # nophone = fields.Integer(string="No. Telpon") 
    # umur = fields.Integer(string="Umur")
    # goldarah = fields.Char(string="Golongan Darah")
    # kotatinggal = fields.Char(string="Kota Asal")
    # komplain = fields.Selection([
    #     ('gigi', "Kesehatan Gigi"),
    #     ('umum', "Sakit mata, Nyeri Sendi atau Otot, Alergi, Batuk dan Pilek, Demam, Masalah Kulit, Penyakit pada paru-paru, Migrain, Hipertensi, Gangguan tidur, Masalah pencernaan, Penyakit menular seksual, Infeksi bakteri, jamur, dan parasit."),
    # ], string="Keluhan", required=True, default="gigi") 



class PoliklinikPendaftaran(models.Model):
    _name = 'poliklinik.pendaftaran'
    _rec_name = 'no'

    # Registrasi Pasien
    no = fields.Char(string="No Antrian",default="/", readonly=True)
    nama = fields.Many2one('res.partner', string="Nama", required=True, domain=[('title', '=', 'Pasien')])
    nophone = fields.Integer(string="No. Telpon") 
    umur = fields.Integer(string="Umur")
    goldarah = fields.Char(string="Golongan Darah")
    kotatinggal = fields.Char(string="Kota Asal")
    komplain = fields.Selection([
        ('gigi', "Kesehatan Gigi"),
        ('umum', "Sakit mata, Nyeri Sendi atau Otot, Alergi, Batuk dan Pilek, Demam, Masalah Kulit, Penyakit pada paru-paru, Migrain, Hipertensi, Gangguan tidur, Masalah pencernaan, Penyakit menular seksual, Infeksi bakteri, jamur, dan parasit."),
    ], string="Keluhan", required=True, default="gigi") 
    # tekananjantung = fields.

    # Penanganan
    namadokter = fields.Many2one('res.partner', string="Nama Dokter", readonly=True)
    bidangdokter = fields.Char(string="Bidang Dokter", readonly=True)
    umurdokter = fields.Integer(string="Umur", readonly=True)
    jadwaldokter = fields.Integer(string="Jadwal Dokter", readonly=True)
    akhirjadwaldokter = fields.Integer(string="Jadwal Selesai Dokter", readonly=True)

    # rencana nanti untuk fields yang dibawah ini
    # hadirdokter = fields.Char(string="Kehadiran Dokter")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),  
        ('done', 'Done'),
        ], string='status', copy=False, default='draft', track_visibility='onchange')

    @api.model
    def create(self, vals):
        # Override the original create function for the res.partner model
        vals['no'] = self.env['ir.sequence'].next_by_code('poliklinik.pendaftaran')
        return super(PoliklinikPendaftaran, self).create(vals)
    
    @api.multi
    def action_confirm(self):
        self.write({'state' : 'open'})
        print ("##############################")
        print ("masuk confirm")
        print ("##############################")

    @api.multi
    def action_cancel(self):
        self.write({'state' : 'draft'})
        print ("##############################")
        print ("masuk cancel")
        print ("##############################")

    @api.multi
    def action_print_data_pasien(self):
        self.write({'state' : 'open'})
        print ("##############################")
        print ("masuk cancel")
        print ("##############################")


    @api.multi
    def action_close(self):
        self.write({'state' : 'done'})
        print ("##############################")
        print ("masuk close")
        print ("##############################")


    
    # bidangdokter = fields.Selection([
    #     ('umum', 'Dokter Umum'),
    #     ('gigi', 'Dokter Gigi'),
    # ], string="Bidang Dokter", required=True)


    # patient_age = fields.Integer(string="Age")
    # notes = fields.Text(string="Notes")
    # image = fields.Binary(string="KTP / KK")
    # doctor = fields.Many2one('res.partner', 'Doctor')

    # state = fields.Selection([
    #     ('draft', 'Draft'),
    #     ('open', 'Confirmed'),
    #     ('done', 'Done'),
    # ], string='Status', readonly=True, copy=False, default='draft', track_visibility='onchange')

    # @api.model
    # def create(self, vals):
    #     # Override the original create function for the res.partner model
    #     vals['no'] = self.env['ir.sequence'].next_by_code('mqpoliklinik.patient')
    #     return super(mqpoliklinik, self).create(vals)

    

# class Partner(models.Model):
#     _inherit = 'res.partner'
#     _rec_name = 'no'
    
#     no = fields.Char(string="No Patient",default="/", readonly=True)
#     noktp = fields.Char(string="No KTP")
#     gender = fields.Selection([('ml', 'Male'),('fm', 'Female')], string="Gender")
#     age = fields.Integer(string="Age")
#     kk = fields.Binary(string="KTP / KK")
#     norek = fields.Integer(string="Nomor Rekening", default=100)
#     doctor = fields.Boolean(String="Doctor", default=True)
#     patient = fields.Boolean(String="Patient")
    

#     @api.model
#     def create(self, vals):
#         # Override the original create function for the res.partner model
#         vals['no'] = self.env['ir.sequence'].next_by_code('res.partner')
#         return super(Partner, self).create(vals)
    
