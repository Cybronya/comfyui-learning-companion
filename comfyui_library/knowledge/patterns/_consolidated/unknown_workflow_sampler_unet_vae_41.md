---
name: unknown_workflow_sampler_unet_vae_41
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.841769
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/h3_r2v_runninghub_tts_v2_2093887746086625282.json, 视频生成/图生视频/h3_r2v_runninghub_tts_v2_fuben1_api_2091063408224460801.json, 视频生成/图生视频/h3参考生视频_2110215490152001538.json, 视频生成/图生视频/minimax_h3_ref2v_3_2092280813852385282.json, 视频生成/图生视频/minimax_h3_ref2v_4_2092280828972855298.json, 视频生成/图生视频/minimax_h3_ref2v_5_2092280840322637826.json, 视频生成/图生视频/minimax_h3_ref2v_6_2092280852507095041.json, 视频生成/图生视频/minimax_h3_全能参考_2084540405961543681.json, 视频生成/图生视频/minimax_h3_全能参考生视频_2084112691525939201.json, 视频生成/图生视频/minimax_h3_全能参考视频_2084269876935479297.json, 视频生成/图生视频/minimax_h3_多图参考生视频_2097588393667551233.json, 视频生成/图生视频/海螺Minimax H3_r2v 官方加速版_2091451868676452353.json, 视频生成/文生视频/azheng_2095047905232121858.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_41

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/h3_r2v_runninghub_tts_v2_2093887746086625282.json、视频生成/图生视频/h3_r2v_runninghub_tts_v2_fuben1_api_2091063408224460801.json、视频生成/图生视频/h3参考生视频_2110215490152001538.json、视频生成/图生视频/minimax_h3_ref2v_3_2092280813852385282.json、视频生成/图生视频/minimax_h3_ref2v_4_2092280828972855298.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 12/13 个有
- `LoraLoaderModelOnly` —— 5/13 个有
- `ComfySwitchNode` —— 4/13 个有
- `PrimitiveBoolean` —— 4/13 个有
- `PrimitiveInt` —— 4/13 个有
- `LoadAudio` —— 3/13 个有
- `MiniMaxH3AudioLatentControlT8` —— 2/13 个有
- `easy downloadIndexTTSAndLoadModel` —— 2/13 个有
- `easy indexTTSAudioMerge` —— 2/13 个有
- `easy indexTTSGenerate` —— 2/13 个有
- `EmptyAudio` —— 1/13 个有
- `MiniMaxH3AddGuide` —— 1/13 个有
- `VideoCombineV2` —— 1/13 个有
- `easy indexTTSEmotionText` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
