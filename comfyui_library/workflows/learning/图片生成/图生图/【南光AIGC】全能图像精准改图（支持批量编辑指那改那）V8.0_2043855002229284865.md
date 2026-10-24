---
key: 图片生成/图生图/【南光AIGC】全能图像精准改图（支持批量编辑指那改那）V8.0_2043855002229284865.json
name: 【南光AIGC】全能图像精准改图（支持批量编辑指那改那）V8.0_2043855002229284865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【南光AIGC】全能图像精准改图（支持批量编辑指那改那）V8.0_2043855002229284865.json
hash: d09525674b19d14e
coverage: 0.928571
learned_at: 2026-10-23 11:49:45
nodes: [PreviewImage, LoadImage, MaskColorize, SaveImage, LoadImage, MaskColorize, LoadImage, MaskColorize, LoadImage, MaskColorize, LoadImage, RH_Nano_Banana_Image2Image, ImageConcanate, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/【南光AIGC】全能图像精准改图（支持批量编辑指那改那）V8.0_2043855002229284865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【南光AIGC】全能图像精准改图（支持批量编辑指那改那）V8.0_2043855002229284865.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（14 个）：
- `PreviewImage`
- `LoadImage`
- `MaskColorize`
- `SaveImage`
- `LoadImage`
- `MaskColorize`
- `LoadImage`
- `MaskColorize`
- `LoadImage`
- `MaskColorize`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `ImageConcanate`
- `SaveImage`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`LoadImage`、`MaskColorize`、`SaveImage`、`RH_Nano_Banana_Image2Image`、`ImageConcanate`

**用到的条目**：LoadImage、SaveImage、ImageConcanate、RH_Nano_Banana_Image2Image、MaskColorize、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
