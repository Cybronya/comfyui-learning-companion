---
name: unknown_workflow_lora_sampler_unet_400
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.828
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, GetImageSize, GetVideoComponents, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, Video Slice]
problems: []
missing: []
members: [平台全量/视频深度图替换人物minimax_2105673804142956545.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-动作迁移-生成视频-工作流_2093578653677481986.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_400

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频深度图替换人物minimax_2105673804142956545.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-动作迁移-生成视频-工作流_2093578653677481986.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `GetImageSize`
- `GetVideoComponents`
- `KSamplerSelect`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `Video Slice`

**可变部分**（部分 workflow 才有）：
- `DA3Inference` —— 1/2 个有
- `DA3Render` —— 1/2 个有
- `ImageBatch` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `LoadDA3Model` —— 1/2 个有
- `MiniMaxH3AddGuide` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RepeatImageBatch` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `VideoFrameSample` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
