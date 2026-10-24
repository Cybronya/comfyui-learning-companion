# TTP_Smart_Tile_Interactive_Crop_Experimental

## 节点类型

`TTP_Smart_Tile_Interactive_Crop_Experimental`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `source_image:IMAGE`（1 次）
- `vision_model:MODEL`（1 次）
- `vision_conditioning:CONDITIONING`（1 次）
- `clip:CLIP`（1 次）
- `qwen_vl_model:TTP_QWENVL3_MODEL`（1 次）
- `image:COMBO`（1 次）
- `layout_json:STRING`（1 次）
- `default_pad:INT`（1 次）
- `default_blend:INT`（1 次）
- `include_full_image:BOOLEAN`（1 次）

## 输出

- `source_image:IMAGE`（1 次）
- `tiles:IMAGE`（1 次）
- `tile_set:TTP_SMART_TILE_SET`（1 次）
- `tile_meta:TTP_SMART_TILE_META`（1 次）
- `positions:LIST`（1 次）
- `preview:IMAGE`（1 次）
- `layout_json:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["51b92ac32a99719cd42d158e88d01d110843cd1f9f8575fda900459ad22267bd.jpg", "{\"version\":1,\"type\":\"ttp_smart_tile_inter`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
