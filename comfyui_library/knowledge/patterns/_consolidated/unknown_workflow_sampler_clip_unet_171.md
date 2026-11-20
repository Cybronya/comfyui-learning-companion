---
name: unknown_workflow_sampler_clip_unet_171
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.824
common_nodes: [BasicScheduler, CLIPTextEncode, DualCFGGuider, InstructPixToPixConditioning, KSamplerSelect, LoadImage, QuadrupleCLIPLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/hidream_e1_1.json, comfyui-workflow-templates-json/hidream_e1_full.json, 图片生成/图生图/HiDream-E1.1 FP8版工作流_1947629622461673473.json, 图片生成/图生图/HiDream-E1.1 动漫转真人写实_1947636333943664641.json, 图片生成/图生图/hidream-e1-1_1948276172112179202.json, 图片生成/图生图/hidream_e1_1_2054774511366623233.json, 图片生成/图生图/hidream_e1_full基础工作流_1924295336838221826.json, 平台全量/ComfyUI官方示例17：HiDream-e1图像编辑工作流 _ ComfyUI从入门到精通_1934220476963315713.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_171

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（comfyui-workflow-templates-json/hidream_e1_1.json、comfyui-workflow-templates-json/hidream_e1_full.json、图片生成/图生图/HiDream-E1.1 FP8版工作流_1947629622461673473.json、图片生成/图生图/HiDream-E1.1 动漫转真人写实_1947636333943664641.json、图片生成/图生图/hidream-e1-1_1948276172112179202.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
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
- `ImageScaleToTotalPixels` —— 5/8 个有
- `CFGNorm` —— 3/8 个有
- `ImageScale` —— 3/8 个有
- `PreviewImage` —— 2/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `ModelSamplingSD3` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
