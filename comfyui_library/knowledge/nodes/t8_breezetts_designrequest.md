# T8_BreezeTTS_DesignRequest

## 节点类型

`T8_BreezeTTS_DesignRequest`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 16 个 workflow 中。

## 输入

- `text:STRING`（15 次）
- `voice_description:STRING`（15 次）
- `cfg_scale:FLOAT`（15 次）
- `text:WILDCARD`（1 次）
- `voice_description:WILDCARD`（1 次）

## 输出

- `request:BREEZE_T8_REQUEST`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["[笑] 欢迎使用 Breeze TTS 2。", "一位温柔自信的年轻女性，声音清晰，语气亲切。", 4]`（11 次）
- `["", "", 4]`（3 次）
- `["6日起我国北方地区将迎降雨降温过程。青海、甘肃、内蒙古、华北及东北等地有小到中雨，局地大雨或暴雨。", "一位温柔自信的年轻女性，声音清晰，语气亲切。", 4]`（1 次）
- `[4]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
