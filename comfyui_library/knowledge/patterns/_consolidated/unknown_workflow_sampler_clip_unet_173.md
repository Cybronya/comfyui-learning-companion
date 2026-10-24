---
name: unknown_workflow_sampler_clip_unet_173
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.822714
common_nodes: [BasicScheduler, CLIPTextEncode, DualCFGGuider, InstructPixToPixConditioning, KSamplerSelect, LoadImage, QuadrupleCLIPLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/hidream_e1_1.json, comfyui-workflow-templates-json/hidream_e1_full.json, 图片生成/图生图/HiDream-E1.1 FP8版工作流_1947629622461673473.json, 图片生成/图生图/HiDream-E1.1 动漫转真人写实_1947636333943664641.json, 图片生成/图生图/hidream-e1-1_1948276172112179202.json, 图片生成/图生图/hidream_e1_1_2054774511366623233.json, 图片生成/图生图/hidream_e1_full基础工作流_1924295336838221826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_173

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（comfyui-workflow-templates-json/hidream_e1_1.json、comfyui-workflow-templates-json/hidream_e1_full.json、图片生成/图生图/HiDream-E1.1 FP8版工作流_1947629622461673473.json、图片生成/图生图/HiDream-E1.1 动漫转真人写实_1947636333943664641.json、图片生成/图生图/hidream-e1-1_1948276172112179202.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCFGGuider`
- `InstructPixToPixConditioning`
- `KSamplerSelect`
- `LoadImage`
- `QuadrupleCLIPLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 5/7 个有
- `CFGNorm` —— 3/7 个有
- `ImageScale` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `ModelSamplingSD3` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
