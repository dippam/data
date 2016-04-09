#! /usr/bin/env python

import json
from sqlobject import *

sqlhub.processConnection = connectionForURI('sqlite:/../../../api/db/development.sqlite3')

class EppiBreviate(SQLObject):
    rid = IntCol()
    title = StringCol()
    volume_id = IntCol()
    name = StringCol()
    year = StringCol()
    keywords = StringCol()

class EppiDoctype(SQLObject):
    rid = IntCol()
    name = StringCol()

class EppiDocument(SQLObject):
    rid = IntCol()
    paper_no = StringCol()
    authoritative_ref = StringCol()
    title_actual = StringCol()
    corp_authors = StringCol()
    personal_author = StringCol()
    publisher = StringCol()
    breviate_page = StringCol()
    tables = StringCol()
    series = StringCol()
    chairman = StringCol()
    abstract = StringCol()
    pages_sectioned = StringCol()
    held_by = StringCol()
    additional_components = StringCol()
    start_page = StringCol()
    vol = StringCol()
    subvol_arabic = StringCol()
    eppi_lc_subject_id = IntCol()
    published = StringCol()
    appointed = StringCol()
    source = StringCol()
    eppi_session_id = IntCol()
    eppi_doctype_id = IntCol()
    eppi_breviate_id = IntCol()
    session = StringCol()
    doctype = StringCol()
    date_appointed = StringCol()
    lc_subject_heading = StringCol()
    breviate_keywords = StringCol()
    breviate_title = StringCol()
    breviate_volume = StringCol()
    vol_arabic = StringCol()
    session_old = StringCol()
    session_year_from = StringCol()
    session_year_to = StringCol()
    date_published = StringCol()

class EppiKeyword(SQLObject):
    rid = IntCol()    
    name = StringCol()

class EppiLcSubject(SQLObject):
    rid = IntCol()
    name = StringCol()
    lft = IntCol()
    rgt = IntCol()
    parent_id = IntCol()
    full_name = StringCol()

class EppiPage(SQLObject):
    rid = IntCol()
    eppi_document_id = IntCol()
    ordinal = IntCol()
    text = StringCol()

class EppiSession(SQLObject):
    rid = IntCol()
    from = StringCol()
    to = StringCol()

class EppiVolume(SQLObject):
    rid = IntCol()
    name = StringCol()

class IedCatFile(SQLObject):
    rid = IntCol()
    filename = StringCol()
    filesize = StringCol()
    ied_cat_files = StringCol()
    description = StringCol()
    category_id = IntCol()

class IedCatalogue(SQLObject):
    rid = IntCol()
    title = StringCol()
    source = StringCol()
    archive = StringCol()
    serial = StringCol()
    catdate = StringCol()
    tags = StringCol()
    transcript = StringCol()

class IedCategory(SQLObject):
    rid = IntCol()
    code = StringCol()
    name = StringCol()
    reference = StringCol()
    description = StringCol()
    show = BoolCol()

class IedEnclosure(SQLObject):
    rid = IntCol()
    ied_record_id = StringCol()
    filename = StringCol()
    label = StringCol()
    image_file_name = StringCol()
    image_content_type = StringCol()
    image_file_size = IntCol()
    image_updated_at = DateTimeCol()

class IedInstitution(SQLObject):
    rid = IntCol()
    name = StringCol()

class IedPage(SQLObject):
    rid = IntCol()
    document_id = IntCol()
    ordinal = IntCol()
    content = StringCol()
    
class IedRecord(SQLObject):
    rid = IntCol()
    uuid = StringCol()
    name = StringCol()
    srcdoc = StringCol()
    source = StringCol()
    added = StringCol()
    chapcode = StringCol()
    transcript = StringCol()
    institution_id = IntCol()
    ied_chapter_id = IntCol()
    ied_chapcode = StringCol()
    timestamp = DateCol()
    archive = StringCol()
    serial = StringCol()
    recorddate = StringCol()
    recordlog = StringCol()
    recordtype = StringCol()
    catid = StringCol()
    partialdate = StringCol()

class Page(SQLObject):
    rid = IntCol()
    document_id = IntCol()
    ordinal = IntCol()
    chapter_id = IntCol()
    record_id = IntCol()
    eppi_document_id = IntCol()

class Place(SQLObject):
    rid = IntCol()
    name = StringCol()
    lat = FloatCol()
    lng = FloatCol()

class SummaryDocument(SQLObject):
    rid = IntCol()
    title = StringCol()
    source_id = IntCol()
    source_type = StringCol()
    boost = IntCol()

class VmrDenomination(SQLObject):
    rid = IntCol()
    name = StringCol()

class VmrDestinationList(SQLObject):
    rid = IntCol()
    place_id = IntCol()
    position_id = IntCol()
    vmr_interview_id = IntCol()

class VmrInterview(SQLObject):
    rid = IntCol()
    code = StringCol()
    summary = StringCol()
    vmr_denomination_id = IntCol()
    gender = StringCol()
    birthplace_id = IntCol()
    residence_id = IntCol()
    childhood_residence_id = IntCol()
    duration = StringCol()
    date = DateCol()
    age_group = IntCol()
    emigration_decade = IntCol()
    return_decade = IntCol()

class VmrKeyword(SQLObject):
    rid = IntCol()
    name = StringCol()

class VmrTrack(SQLObject):
    rid = IntCol()
    track_id = IntCol()
    track_no = IntCol()
    duration = StringCol()
    keywords = StringCol()
    vmr_interview_id = IntCol()
    
class JSONExtractor    
    def Main():
        rows = VmrTrack.select()
        items = []
        
        for row in rows:
            items.append = { 'track_id' : row.track_id, 'track_no' : row.track_no, 'duration' : row.duration, 'keywords' : row.keywords, 'vmr_interview_id' : row.vmr_interview_id }

        print simplejson.dumps(items)
