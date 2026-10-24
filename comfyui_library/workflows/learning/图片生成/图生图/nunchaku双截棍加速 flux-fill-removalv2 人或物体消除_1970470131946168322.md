---
key: 图片生成/图生图/nunchaku双截棍加速 flux-fill-removalv2 人或物体消除_1970470131946168322.json
name: nunchaku双截棍加速 flux-fill-removalv2 人或物体消除_1970470131946168322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/nunchaku双截棍加速 flux-fill-removalv2 人或物体消除_1970470131946168322.json
hash: a3c0d03b99bccb14
coverage: 1
learned_at: 2026-10-23 11:41:24
nodes: [CLIPTextEncodeFlux, NunchakuFluxDiTLoader, VAELoader, DeepTranslatorTextNode, NunchakuFluxLoraLoader, CLIPTextEncode, LoadImage, SaveImage, ImageConcatMulti, SaveImage, KSamplerAdvanced, InpaintModelConditioning, VAEDecode, DualCLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 25, "denoise": "normal", "sampler_name": 8, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/nunchaku双截棍加速 flux-fill-removalv2 人或物体消除_1970470131946168322.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/nunchaku双截棍加速 flux-fill-removalv2 人或物体消除_1970470131946168322.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPTextEncodeFlux` ★核心
- `NunchakuFluxDiTLoader`
- `VAELoader`
- `DeepTranslatorTextNode`
- `NunchakuFluxLoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SaveImage`
- `ImageConcatMulti`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `InpaintModelConditioning`
- `VAEDecode` ★核心
- `DualCLIPLoader`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `25`
- `sampler_name` = `8`
- `scheduler` = `euler_ancestral`
- `denoise` = `normal`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPTextEncodeFlux`、`NunchakuFluxDiTLoader`、`VAELoader`、`DeepTranslatorTextNode`、`NunchakuFluxLoraLoader`、`CLIPTextEncode`、`LoadImage`、`SaveImage`、`ImageConcatMulti`、`KSamplerAdvanced`、`InpaintModelConditioning`、`VAEDecode`、`DualCLIPLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、KSamplerAdvanced、CLIPTextEncodeFlux、NunchakuFluxLoraLoader、DualCLIPLoader
