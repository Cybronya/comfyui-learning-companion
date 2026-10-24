---
name: unknown_workflow_sampler_unet_vae_119
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.809667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/minimaxH3文生+参考生视频_2084286286344581121.json, 视频生成/文生视频/minimaxH3满血版海螺H3_2085024933234692098.json, 视频生成/文生视频/minimax_h3_t2v文生视频_2084177287007784961.json, 视频生成/文生视频/minimax_h3_文生_图生视频_2084261498850988033.json, 视频生成/文生视频/minimax_h3_文生视频_2084110685591654402.json, 视频生成/文生视频/video_minimax_h3_r2v 多素材联合参考_2085213870431490049.json, 视频生成/文生视频/video_minimax_h3_r2v多参=加速_2095122591458615297.json, 视频生成/文生视频/多参生视频-MiniMax_h3_r2v-视频音频图片参考-智能提示词_2084694636374872065.json, 视频生成/文生视频/智能提示词-多参生视频-MiniMax_h3_r2v-视频音频图片参考_2084262166823268354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_119

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/minimaxH3文生+参考生视频_2084286286344581121.json、视频生成/文生视频/minimaxH3满血版海螺H3_2085024933234692098.json、视频生成/文生视频/minimax_h3_t2v文生视频_2084177287007784961.json、视频生成/文生视频/minimax_h3_文生_图生视频_2084261498850988033.json、视频生成/文生视频/minimax_h3_文生视频_2084110685591654402.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
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
- `LoadImage` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `MiniMaxH3ReferenceToVideo` —— 6/9 个有
- `VHS_LoadVideo` —— 5/9 个有
- `LoadAudio` —— 4/9 个有
- `MiniMaxH3ImageToVideo` —— 4/9 个有
- `LoadVideo` —— 3/9 个有
- `AudioCrop` —— 2/9 个有
- `RH_LLMAPI_Pro_Node` —— 2/9 个有
- `easy anythingIndexSwitch` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `孤海注释` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `GetImageSize` —— 1/9 个有
- `H3SigmaRefiner` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `LoraLoaderModelOnly` —— 1/9 个有
- `ModelAttentionBackend` —— 1/9 个有
- `TextInput_` —— 1/9 个有
- `easy positive` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
