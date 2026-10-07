# ChinesePrompt_Mix

## 节点类型

`ChinesePrompt_Mix`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `text:STRING`（2 次）
- `seed:INT`（1 次）

## 输出

- `prompt:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["日本的富士山风光，湖水，村庄，雪山，蓝天和白云", "off", 675734596094626, "randomize", [false, true]]`（1 次）
- `["一位年轻的亚洲女性在冰冻的湖面上行走，正对对着相机。此人穿着棕色夹克、米色围巾和米色裙子。", "off", 635801905611971, "fixed", [false, true]]`（1 次）
- `["高清手机壁纸", "off", 914391299188454, "randomize"]`（1 次）
- `["", "off", 173188046510758, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
