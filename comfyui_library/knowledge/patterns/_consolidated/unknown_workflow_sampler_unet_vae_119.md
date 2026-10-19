---
name: unknown_workflow_sampler_unet_vae_119
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.820833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/h3_r2v_runninghub_tts_v2_2093887746086625282.json, 视频生成/图生视频/h3_r2v_runninghub_tts_v2_fuben1_api_2091063408224460801.json, 视频生成/图生视频/h3参考生视频_2110215490152001538.json, 视频生成/图生视频/minimax 1.0 8步加速1.0正式版_2088137884623785985.json, 视频生成/图生视频/minimax_h3_图生视频_牛来_2094972668582916098.json, 视频生成/图生视频/minimax_h3_多图参考生视频_2097588393667551233.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_119

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/h3_r2v_runninghub_tts_v2_2093887746086625282.json、视频生成/图生视频/h3_r2v_runninghub_tts_v2_fuben1_api_2091063408224460801.json、视频生成/图生视频/h3参考生视频_2110215490152001538.json、视频生成/图生视频/minimax 1.0 8步加速1.0正式版_2088137884623785985.json、视频生成/图生视频/minimax_h3_图生视频_牛来_2094972668582916098.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
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
- `CreateVideo` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxH3ReferenceToVideo` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `LoadAudio` —— 4/6 个有
- `ComfySwitchNode` —— 3/6 个有
- `PrimitiveBoolean` —— 3/6 个有
- `PrimitiveInt` —— 3/6 个有
- `MiniMaxH3AudioLatentControlT8` —— 2/6 个有
- `easy downloadIndexTTSAndLoadModel` —— 2/6 个有
- `easy indexTTSAudioMerge` —— 2/6 个有
- `easy indexTTSGenerate` —— 2/6 个有
- `EmptyAudio` —— 1/6 个有
- `MiniMaxH3AddGuide` —— 1/6 个有
- `MiniMaxH3ImageToVideo` —— 1/6 个有
- `SolAttnPatch` —— 1/6 个有
- `VideoCombineV2` —— 1/6 个有
- `easy indexTTSEmotionText` —— 1/6 个有
- `孤海注释` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
