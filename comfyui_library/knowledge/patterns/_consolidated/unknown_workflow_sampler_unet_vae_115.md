---
name: unknown_workflow_sampler_unet_vae_115
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.807857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax-H3 I2V多图参考(多重加速组合)_2085771805838635009.json, 视频生成/图生视频/MiniMax-H3 Ref2va 参考生视频标准版_2095421074551951361.json, 视频生成/图生视频/MiniMax-H3 人物配音+音轨时间控制_2085547178214383618.json, 视频生成/图生视频/MiniMax-H3 多参单人声音克隆ref2va_2085616446960390146.json, 视频生成/图生视频/MiniMax-H3 多图参考动作迁移_2084482324229615618.json, 视频生成/图生视频/MiniMax-H3 多图参考角色声音克隆(8步加速)_2085281923852759041.json, 视频生成/图生视频/MiniMax-H3 多图参考角色配音(8步加速)_2085223284391628802.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_115

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3 I2V多图参考(多重加速组合)_2085771805838635009.json、视频生成/图生视频/MiniMax-H3 Ref2va 参考生视频标准版_2095421074551951361.json、视频生成/图生视频/MiniMax-H3 人物配音+音轨时间控制_2085547178214383618.json、视频生成/图生视频/MiniMax-H3 多参单人声音克隆ref2va_2085616446960390146.json、视频生成/图生视频/MiniMax-H3 多图参考动作迁移_2084482324229615618.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
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
- `AnySwitch` —— 6/7 个有
- `Fast Bypasser (rgthree)` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `MiniMaxH3BlockCacheT8` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `LoadAudio` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `RMBG` —— 5/7 个有
- `TTP_text_mix` —— 5/7 个有
- `TrimAudioDuration` —— 4/7 个有
- `GetVideoComponents` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `VRAM_Debug` —— 3/7 个有
- `1hew_AudioDuration` —— 2/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `AudioConcat` —— 1/7 个有
- `EasyCache` —— 1/7 个有
- `EmptyAudio` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `Int` —— 1/7 个有
- `LoadVideo` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有
- `PreviewAudio` —— 1/7 个有
- `SpectrumApplyMiniMaxH3` —— 1/7 个有
- `VHS_GetImageCount` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
