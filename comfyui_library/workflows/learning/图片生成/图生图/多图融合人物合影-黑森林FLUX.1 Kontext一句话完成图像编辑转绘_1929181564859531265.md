---
key: 图片生成/图生图/多图融合人物合影-黑森林FLUX.1 Kontext一句话完成图像编辑转绘_1929181564859531265.json
name: 多图融合人物合影-黑森林FLUX.1 Kontext一句话完成图像编辑转绘_1929181564859531265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图融合人物合影-黑森林FLUX.1 Kontext一句话完成图像编辑转绘_1929181564859531265.json
hash: 78b35864ab70cbd0
coverage: 0.764706
learned_at: 2026-10-23 12:45:17
nodes: [easy imageScaleDownToSize, SaveImage, SaveImage, LayerUtility: ImageRemoveAlpha, InspyrenetRembg, Segment, PrimitiveString, RH_ComfyFluxKontext, PreviewImage, BiRefNet_Hugo, ImageConcanate, PreviewImage, LoadImage, ImageConcanate, LoadImage, DeepTranslatorTextNode, easy showAnything]
patterns: []
missing: []
---

# 图片生成/图生图/多图融合人物合影-黑森林FLUX.1 Kontext一句话完成图像编辑转绘_1929181564859531265.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图融合人物合影-黑森林FLUX.1 Kontext一句话完成图像编辑转绘_1929181564859531265.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（17 个）：
- `easy imageScaleDownToSize`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageRemoveAlpha`
- `InspyrenetRembg`
- `Segment`
- `PrimitiveString`
- `RH_ComfyFluxKontext`
- `PreviewImage`
- `BiRefNet_Hugo`
- `ImageConcanate`
- `PreviewImage`
- `LoadImage`
- `ImageConcanate`
- `LoadImage`
- `DeepTranslatorTextNode`
- `easy showAnything`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`easy imageScaleDownToSize`、`SaveImage`、`LayerUtility: ImageRemoveAlpha`、`InspyrenetRembg`、`Segment`、`RH_ComfyFluxKontext`、`BiRefNet_Hugo`、`ImageConcanate`、`LoadImage`、`DeepTranslatorTextNode`

**用到的条目**：LoadImage、RH_ComfyFluxKontext、easy imageScaleDownToSize、SaveImage、ImageConcanate、InspyrenetRembg、DeepTranslatorTextNode、BiRefNet_Hugo
