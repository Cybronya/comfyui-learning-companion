---
name: unknown_workflow_sampler_unet_vae_103
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.855857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3多参_2085409741941067777.json, 视频生成/图生视频/MinimaxI2V_2084500141607841794.json, 视频生成/图生视频/i2va_minimax_h3_vaeint8_api_2103863320280391681.json, 视频生成/图生视频/加速高质开源MiniMax+H3+FL2VA开源版-首尾帧参考生视频+++_2084152775365189633.json, 视频生成/图生视频/无参考视频-新加速高质开源MiniMax H3 RE2VA开源版_2087442373067501569.json, 视频生成/图生视频/超级融合模型-高质量(10Eros-Max)Minimax BF16参考生视频-加速版-TEST3版_2086762633667108866.json, 视频生成/文生视频/多图参考H3广告_2085248140055236609.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_103

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3多参_2085409741941067777.json、视频生成/图生视频/MinimaxI2V_2084500141607841794.json、视频生成/图生视频/i2va_minimax_h3_vaeint8_api_2103863320280391681.json、视频生成/图生视频/加速高质开源MiniMax+H3+FL2VA开源版-首尾帧参考生视频+++_2084152775365189633.json、视频生成/图生视频/无参考视频-新加速高质开源MiniMax H3 RE2VA开源版_2087442373067501569.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 5/7 个有
- `MiniMaxH3BlockCacheT8` —— 5/7 个有
- `PreviewAny` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `MiniMaxH3ImageToVideo` —— 3/7 个有
- `MiniMaxH3ReferenceToVideo` —— 3/7 个有
- `RHLLMChatNode` —— 3/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `CR Text` —— 1/7 个有
- `EasyCache` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `VHS_VideoInfo` —— 1/7 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 0 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
