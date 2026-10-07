# TT_img_enc_v2

## 节点类型

`TT_img_enc_v2`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `images:IMAGE`（4 次）
- `audio:AUDIO`（4 次）
- `fps:FLOAT`（4 次）
- `video_compression:INT`（4 次）
- `png_compression:INT`（4 次）
- `skip_watermark_area:BOOLEAN`（4 次）
- `usage_notes:STRING`（4 次）
- `password:STRING`（1 次）
- `title:STRING`（1 次）

## 输出

- `IMAGE:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[16, 19, 6, true, "解码教程：https://www.bilibili.com/video/BV1Tq42zZEPK/\n"]`（3 次）
- `[16, 19, 6, true, "", "", "此节点仅用于用户隐私保护，使用即承诺合法合规使用本工具，自愿承担全部风险与责任\n建议设置密码，可以更大程度提升隐私保护安全性\n需配合专业隐私保护小程序TT Tool使用\nvideo`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
