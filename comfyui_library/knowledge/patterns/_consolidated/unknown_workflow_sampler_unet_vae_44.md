---
name: unknown_workflow_sampler_unet_vae_44
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.8042
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, Fast Groups Bypasser (rgthree), KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 I2V多图参考(多重加速组合)_2085771805838635009.json, 视频生成/图生视频/MiniMax-H3 人物配音+音轨时间控制_2085547178214383618.json, 视频生成/图生视频/MiniMax-H3 多参单人声音克隆ref2va_2085616446960390146.json, 视频生成/图生视频/MiniMax-H3 多图参考动作迁移_2084482324229615618.json, 视频生成/图生视频/MiniMax-H3 多图参考角色声音克隆(8步加速)_2085281923852759041.json, 视频生成/图生视频/MiniMax-H3 多图参考角色配音(8步加速)_2085223284391628802.json, 视频生成/图生视频/MiniMax-H3 视频参考生视频_2084299226577719298.json, 视频生成/图生视频/MiniMax-H3多参格斗动作迁移+背景替换(8步加速)_2085363724478672897.json, 视频生成/图生视频/MiniMax-H3多参格斗动作迁移+背景替换(8步加速)_2089269367602237441.json, 视频生成/图生视频/MiniMax-H3多参格斗动作迁移+背景替换(加速版)_2087074703075790850.json, 视频生成/图生视频/MiniMax-H3开源版 多参格斗动作迁移+背景替换(8步加速)_2085695540532178945.json, 视频生成/图生视频/MiniMax-H3开源版 多参格斗动作迁移+背景替换(8步加速)_2093664887015821313.json, 视频生成/图生视频/（8步加速)MiniMax-H3开源版 多参格斗动作迁移+背景替换 图生视频_2093641083233333249.json, 视频生成/图生视频/（8步加速)MiniMax-H3开源版 多参格斗动作迁移+背景替换_2085703980176465922.json, 视频生成/文生视频/MiniMax-H3 视频参考生视频_2089945535112372225.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_44

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 I2V多图参考(多重加速组合)_2085771805838635009.json、视频生成/图生视频/MiniMax-H3 人物配音+音轨时间控制_2085547178214383618.json、视频生成/图生视频/MiniMax-H3 多参单人声音克隆ref2va_2085616446960390146.json、视频生成/图生视频/MiniMax-H3 多图参考动作迁移_2084482324229615618.json、视频生成/图生视频/MiniMax-H3 多图参考角色声音克隆(8步加速)_2085281923852759041.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
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
- `PreviewImage` —— 14/15 个有
- `MiniMaxH3BlockCacheT8` —— 13/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/15 个有
- `GetVideoComponents` —— 12/15 个有
- `LoraLoaderModelOnly` —— 12/15 个有
- `RMBG` —— 12/15 个有
- `VRAM_Debug` —— 12/15 个有
- `ImageConcatMulti` —— 11/15 个有
- `GetImageRangeFromBatch` —— 10/15 个有
- `Int` —— 10/15 个有
- `VHS_LoadVideo` —— 10/15 个有
- `VHS_GetImageCount` —— 8/15 个有
- `ImageResizeKJv2` —— 7/15 个有
- `AnySwitch` —— 6/15 个有
- `Fast Bypasser (rgthree)` —— 6/15 个有
- `TTP_text_mix` —— 5/15 个有
- `LoadAudio` —— 4/15 个有
- `TrimAudioDuration` —— 4/15 个有
- `EasyCache` —— 3/15 个有
- `PathchSageAttentionKJ` —— 3/15 个有
- `PreviewAny` —— 3/15 个有
- `1hew_AudioDuration` —— 2/15 个有
- `SDVN Any Show` —— 2/15 个有
- `VHS_VideoInfo` —— 2/15 个有
- `AudioConcat` —— 1/15 个有
- `EmptyAudio` —— 1/15 个有
- `PreviewAudio` —— 1/15 个有
- `SpectrumApplyMiniMaxH3` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
