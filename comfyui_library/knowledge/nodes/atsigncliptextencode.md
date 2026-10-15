# AtSignCLIPTextEncode

## 节点类型

`AtSignCLIPTextEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `1:IMAGE`（1 次）
- `2:IMAGE`（1 次）
- `3:IMAGE`（1 次）
- `4:IMAGE`（1 次）
- `clip:CLIP`（1 次）
- `background:IMAGE`（1 次）
- `map_config:STRING`（1 次）
- `text:STRING`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）
- `parsed_text:STRING`（1 次）
- `1_img:IMAGE`（1 次）
- `2_img:IMAGE`（1 次）
- `3_img:IMAGE`（1 次）
- `4_img:IMAGE`（1 次）
- `bg_img:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["@角色A=1\n@背景=bg", "电影级写实风格，院线级色调，人像写实摄影，{确保人物一致性}\n@角色A 站在@背景 窗户旁边看向窗外。角色@角色A 缓慢转头看向镜头，缓缓走进镜头\n台词（标准普通话）：我就是我，上帝啊"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
