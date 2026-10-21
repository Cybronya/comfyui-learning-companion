---
name: unknown_workflow_lora_sampler_clip_176
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6585
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveInt, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux  角色设计专用_2066838182410412034.json, 图片生成/文生图/Flux2_klein-kv模型 图像编辑 ComfyUI 工作流_2033560457822343169.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_176

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux  角色设计专用_2066838182410412034.json、图片生成/文生图/Flux2_klein-kv模型 图像编辑 ComfyUI 工作流_2033560457822343169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `JjkConcat` —— 1/2 个有
- `JoinImages` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SetImageSize` —— 1/2 个有
- `Textbox` —— 1/2 个有
- `ttN text` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
