---
name: unknown_workflow_upscale_latent_upscale_lora_72
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.96325
common_nodes: [BasicGuider, CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, ConcatTextOfUtils, CreateVideo, GetVideoComponents, LTXVConditioning, LTXVLatentUpsampler, LatentUpscaleModelLoader, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3OutputTrimT8, MiniMaxH3SolEngineDraftToLTXT8Advanced, MiniMaxH3SolEngineLTXIdentityRefinerSetupT8Advanced, MiniMaxH3SolEngineTAEHVDecodeT8Advanced, MiniMaxH3SolEngineTAEHVLoaderT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SolAttnMiniMax, UNETLoader, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/MiniMax H3 Super 参考生视频 刘神_2094997522963066882.json, 平台全量/MiniMax H3超级加速-二阶段快速文戏视频工作流_2094998177798778882.json, 视频生成/图生视频/MiniMax H3 Super Acceleration二阶段超级加速（仅适合文戏）_2093866023492603906.json, 视频生成/图生视频/MiniMax H3 二阶超级加速（不适合动作戏）_2095489832930865153.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_72

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/MiniMax H3 Super 参考生视频 刘神_2094997522963066882.json、平台全量/MiniMax H3超级加速-二阶段快速文戏视频工作流_2094998177798778882.json、视频生成/图生视频/MiniMax H3 Super Acceleration二阶段超级加速（仅适合文戏）_2093866023492603906.json、视频生成/图生视频/MiniMax H3 二阶超级加速（不适合动作戏）_2095489832930865153.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `ConcatTextOfUtils`
- `CreateVideo`
- `GetVideoComponents`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3OutputTrimT8`
- `MiniMaxH3SolEngineDraftToLTXT8Advanced`
- `MiniMaxH3SolEngineLTXIdentityRefinerSetupT8Advanced`
- `MiniMaxH3SolEngineTAEHVDecodeT8Advanced`
- `MiniMaxH3SolEngineTAEHVLoaderT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 3/4 个有
- `LoadAudio` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
