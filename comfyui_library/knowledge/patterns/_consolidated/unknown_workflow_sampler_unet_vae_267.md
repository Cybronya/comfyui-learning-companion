---
name: unknown_workflow_sampler_unet_vae_267
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8614
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfySwitchNode, CreateVideo, KSamplerSelect, MiniMaxH3ImageToVideo, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/4步MiniMax-H3视频续写-LynnReal-Omni_2099804328453296130.json, 平台全量/MiniMax-H3视频续写-LynnReal-Omni_2100875133333368834.json, 平台全量/MiniMax-H3视频续写-LynnReal-Omni_2101140128768028674.json, 视频生成/图生视频/4步MiniMax-H3首帧生视频-LynnReal-Omni_2099804258936901633.json, 视频生成/图生视频/LynnReal-Onmi FastH3 V2V视频扩展_2101507749917061121.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_267

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/4步MiniMax-H3视频续写-LynnReal-Omni_2099804328453296130.json、平台全量/MiniMax-H3视频续写-LynnReal-Omni_2100875133333368834.json、平台全量/MiniMax-H3视频续写-LynnReal-Omni_2101140128768028674.json、视频生成/图生视频/4步MiniMax-H3首帧生视频-LynnReal-Omni_2099804258936901633.json、视频生成/图生视频/LynnReal-Onmi FastH3 V2V视频扩展_2101507749917061121.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `CreateVideo`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PrimitiveBoolean`
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
- `AudioConcat` —— 4/5 个有
- `ConcatenateVideo` —— 4/5 个有
- `EmptyAudio` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `GetVideoComponents` —— 4/5 个有
- `ImageFromBatch` —— 4/5 个有
- `ImageScale` —— 4/5 个有
- `LoadVideo` —— 4/5 个有
- `MiniMaxH3AddGuide` —— 4/5 个有
- `TrimAudioDuration` —— 4/5 个有
- `AnySwitch` —— 1/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `GetAudioDurationFromAudio` —— 1/5 个有
- `Int` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
