---
name: unknown_workflow_sampler_unet_vae_157
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.964
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, EasyCache, ImageResizeKJv2, Int, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SaveVideo, ShowAnything|Mie, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, intToFloat _O]
problems: []
missing: []
members: [视频生成/图生视频/minimax角色替换_2106755665564889089.json, 视频生成/文生视频/MiniMax H3 多图参考 音频参考 加速优化版_2091125673569112066.json, 视频生成/文生视频/MiniMax H3 多图参考 音频参考 加速版_2090781925186301953.json, 视频生成/文生视频/minimax角色替换_2106755665564889089.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_157

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/minimax角色替换_2106755665564889089.json、视频生成/文生视频/MiniMax H3 多图参考 音频参考 加速优化版_2091125673569112066.json、视频生成/文生视频/MiniMax H3 多图参考 音频参考 加速版_2090781925186301953.json、视频生成/文生视频/minimax角色替换_2106755665564889089.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `intToFloat _O`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `ImageFromBatch` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `llama_cpp_instruct_adv` —— 2/4 个有
- `llama_cpp_model_loader` —— 2/4 个有
- `llama_cpp_parameters` —— 2/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
