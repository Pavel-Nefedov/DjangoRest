import React from 'react'

const MenuItem = ({menu}) => {
    return (
        <tr>
            <td>
                {menu.home}
            </td>
            <td>
                {menu.catalog}
            </td>
            <td>
                {menu.contacts}
            </td>
            <td>
                {menu.settings}
            </td>
        </tr>
    )
}

const MenuList = ({menus}) => {
    return (
        <table>
            <th>
                Меню
            </th>
            <th>
                Каталог
            </th>
            <th>
                Контакты
            </th>
            <th>
                Настройки
            </th>
            {menus.map((menu) => <MenuItem menu={menu}/>)}
        </table>
    )
}

export default MenuList