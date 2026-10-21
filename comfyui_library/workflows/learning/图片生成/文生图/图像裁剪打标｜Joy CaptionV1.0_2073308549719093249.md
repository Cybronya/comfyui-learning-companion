---
key: 图片生成/文生图/图像裁剪打标｜Joy CaptionV1.0_2073308549719093249.json
name: 图像裁剪打标｜Joy CaptionV1.0_2073308549719093249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图像裁剪打标｜Joy CaptionV1.0_2073308549719093249.json
hash: d830cb7b4e5958cc
coverage: 0.857143
learned_at: 2026-10-20 00:02:18
nodes: [InpaintCrop, PreviewImage, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model, CR Text Concatenate, String, Joy_caption_two_advanced, Joy_extra_options, ImageScale, easy showAnything, LayerMask: SAM2Ultra, Joy_caption_two_load, easy saveText, HAIGC_LoadImagesFromZip]
patterns: []
missing: []
---

# 图片生成/文生图/图像裁剪打标｜Joy CaptionV1.0_2073308549719093249.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图像裁剪打标｜Joy CaptionV1.0_2073308549719093249.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（14 个）：
- `InpaintCrop`
- `PreviewImage`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: LoadFlorence2Model`
- `CR Text Concatenate`
- `String`
- `Joy_caption_two_advanced`
- `Joy_extra_options`
- `ImageScale`
- `easy showAnything`
- `LayerMask: SAM2Ultra`
- `Joy_caption_two_load`
- `easy saveText`
- `HAIGC_LoadImagesFromZip`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`InpaintCrop`、`LayerMask: ObjectDetectorFL2`、`LayerMask: LoadFlorence2Model`、`CR Text Concatenate`、`String`、`Joy_caption_two_advanced`、`Joy_extra_options`、`ImageScale`、`LayerMask: SAM2Ultra`、`Joy_caption_two_load`、`easy saveText`、`HAIGC_LoadImagesFromZip`

**用到的条目**：easy saveText、ImageScale、InpaintCrop、Joy_caption_two_load、Joy_caption_two_advanced、Joy_extra_options、String、HAIGC_LoadImagesFromZip
