---
key: 平台全量/Anything Golden Workflow_1893855655160360961.json
name: Anything Golden Workflow_1893855655160360961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Anything Golden Workflow_1893855655160360961.json
hash: 0305a2abc9a25cc7
coverage: 0.916667
learned_at: 2026-11-14 00:19:22
nodes: [CLIPTextEncode, CR Apply Multi-ControlNet, CLIPTextEncode, BRIA_RMBG_Zho, BRIA_RMBG_ModelLoader_Zho, PreviewImage, VAEDecode, AIO_Preprocessor, AIO_Preprocessor, CR Aspect Ratio, ToBasicPipe, CR Apply LoRA Stack, ImpactKSamplerBasicPipe, CR Text, CR Text Concatenate, CR Multi-ControlNet Stack, HintImageEnchance, LoadImage, CR Text, CheckpointLoaderSimple, PreviewImage, CR Simple Image Compare, SaveImage, CR LoRA Stack]
patterns: []
missing: []
parameters: {"cfg": 5, "checkpoint": "麒麟-revAnimated_v122_V1.2.2.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 786987002803157, "steps": 25}
---

# 平台全量/Anything Golden Workflow_1893855655160360961.json

> 来源文件 `comfyui_library/workflows/平台全量/Anything Golden Workflow_1893855655160360961.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPTextEncode` ★核心
- `CR Apply Multi-ControlNet`
- `CLIPTextEncode` ★核心
- `BRIA_RMBG_Zho`
- `BRIA_RMBG_ModelLoader_Zho`
- `PreviewImage`
- `VAEDecode` ★核心
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `CR Aspect Ratio`
- `ToBasicPipe`
- `CR Apply LoRA Stack`
- `ImpactKSamplerBasicPipe` ★核心
- `CR Text`
- `CR Text Concatenate`
- `CR Multi-ControlNet Stack`
- `HintImageEnchance`
- `LoadImage`
- `CR Text`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `CR Simple Image Compare`
- `SaveImage`
- `CR LoRA Stack`

## 关键参数

- `seed` = `786987002803157`
- `steps` = `25`
- `cfg` = `5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `麒麟-revAnimated_v122_V1.2.2.safetensors`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`CLIPTextEncode`、`CR Apply Multi-ControlNet`、`BRIA_RMBG_Zho`、`BRIA_RMBG_ModelLoader_Zho`、`VAEDecode`、`AIO_Preprocessor`、`CR Aspect Ratio`、`ToBasicPipe`、`CR Apply LoRA Stack`、`ImpactKSamplerBasicPipe`、`CR Text`、`CR Text Concatenate`、`CR Multi-ControlNet Stack`、`HintImageEnchance`、`LoadImage`、`CheckpointLoaderSimple`、`CR Simple Image Compare`、`SaveImage`、`CR LoRA Stack`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CR Apply Multi-ControlNet、CR Multi-ControlNet Stack、ImpactKSamplerBasicPipe、CR Apply LoRA Stack
