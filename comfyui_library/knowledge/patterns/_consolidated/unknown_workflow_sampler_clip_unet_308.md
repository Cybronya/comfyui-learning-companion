---
name: unknown_workflow_sampler_clip_unet_308
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.867
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/SRPO VS KREA_1967227108663627778.json, 图片生成/文生图/SRPO-image-generation-workflow_1967418961937698817.json, 图片生成/文生图/SRPO-更细腻真实的图片生成模型-文生图工作流_1971799414320852993.json, 图片生成/文生图/文生图-SRPO直出+美学+超真实质感+加速-AIMJ_1968322626772979714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_308

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/SRPO VS KREA_1967227108663627778.json、图片生成/文生图/SRPO-image-generation-workflow_1967418961937698817.json、图片生成/文生图/SRPO-更细腻真实的图片生成模型-文生图工作流_1971799414320852993.json、图片生成/文生图/文生图-SRPO直出+美学+超真实质感+加速-AIMJ_1968322626772979714.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `SeedVR2` —— 2/4 个有
- `Bjornulf_FreeVRAM` —— 1/4 个有
- `Joy_caption` —— 1/4 个有
- `Joy_caption_load` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
