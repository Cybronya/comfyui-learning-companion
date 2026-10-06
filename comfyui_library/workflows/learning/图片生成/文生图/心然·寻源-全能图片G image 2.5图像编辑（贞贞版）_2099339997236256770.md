---
key: 图片生成/文生图/心然·寻源-全能图片G image 2.5图像编辑（贞贞版）_2099339997236256770.json
name: 心然·寻源-全能图片G image 2.5图像编辑（贞贞版）_2099339997236256770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/心然·寻源-全能图片G image 2.5图像编辑（贞贞版）_2099339997236256770.json
hash: c5ff3a4ccd0dcdcc
coverage: 0.5
learned_at: 2026-10-07 03:05:33
nodes: [SaveImage, Note, LoadImage, LoadImage, CR Prompt Text, Note, LoadImage, Zhenzhen_Image_G25_Lowprice, LoadImage, Seedance_Config]
patterns: []
missing: [Zhenzhen_Image_G25_Lowprice, CR Prompt Text, Seedance_Config]
discoveries: [次要节点 `Zhenzhen_Image_G25_Lowprice` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seedance_Config` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/心然·寻源-全能图片G image 2.5图像编辑（贞贞版）_2099339997236256770.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/心然·寻源-全能图片G image 2.5图像编辑（贞贞版）_2099339997236256770.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `SaveImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `Note`
- `LoadImage`
- `Zhenzhen_Image_G25_Lowprice`
- `LoadImage`
- `Seedance_Config`

## 知识

覆盖率 **50%**（5/10）

**有卡**：`SaveImage`、`LoadImage`

**缺卡**（3）：`Zhenzhen_Image_G25_Lowprice`、`CR Prompt Text`、`Seedance_Config`

**用到的条目**：LoadImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora、Text、sampler_name 调整经验、steps 调整经验、cfg 调整经验

## 学习发现

- 次要节点 `Zhenzhen_Image_G25_Lowprice` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seedance_Config` 仅有 KSampler 的通用知识，没有该节点自己的说明
