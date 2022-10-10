import React from 'react'

const FooterItem = ({footer}) => {
    return (
        <tr>
            <td>
                {footer.contact_details}
            </td>
            <td>
                {footer.copyright}
            </td>
        </tr>
    )
}

const FooterList = ({footers}) => {
    return (
        <table>
            <th>
                Контакты
            </th>
            <th>
                Значек копирайта
            </th>
            {footers.map((footer) => <FooterItem footer={footer}/>)}
        </table>
    )
}

export default FooterList