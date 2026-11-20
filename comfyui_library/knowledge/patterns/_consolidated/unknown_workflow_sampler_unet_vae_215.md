---
name: unknown_workflow_sampler_unet_vae_215
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.771143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/开源版Minimax-h3 多模态全能参考版_2084936517058912257.json, 视频生成/图生视频/海螺MiniMax-H3开源版 图片开口说话数字人 图像音频参考生视频_2086786651887587329.json, 视频生成/图生视频/海螺h3 MiniMax-H3开源版 图片开口说话数字人 图像音频参考生视频_2084260160511504385.json, 视频生成/图生视频/老秦的声音克隆数字人_2097164544790589442.json, 视频生成/文生视频/A-5 MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2084649315783503873.json, 视频生成/文生视频/Minimax_h3官方多参视频生成工作流_2084688064726781954.json, 视频生成/文生视频/音频裁剪驱动MiniMax H3数字人-单图版_2090380497007501314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_215

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/开源版Minimax-h3 多模态全能参考版_2084936517058912257.json、视频生成/图生视频/海螺MiniMax-H3开源版 图片开口说话数字人 图像音频参考生视频_2086786651887587329.json、视频生成/图生视频/海螺h3 MiniMax-H3开源版 图片开口说话数字人 图像音频参考生视频_2084260160511504385.json、视频生成/图生视频/老秦的声音克隆数字人_2097164544790589442.json、视频生成/文生视频/A-5 MiniMaxH3 参考生视频（量化加速版） _ 文本 图像 音频 视频_2084649315783503873.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `VAEDecodeAudio` —— 6/7 个有
- `VHS_LoadVideo` —— 3/7 个有
- `AILab_QwenVL` —— 2/7 个有
- `CR Text` —— 2/7 个有
- `JoinStrings` —— 2/7 个有
- `Label (rgthree)` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `PreviewAudio` —— 2/7 个有
- `Any To String (mtb)` —— 1/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `RH_GetAudioDuration` —— 1/7 个有
- `SoundFlow_GetLength` —— 1/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/7 个有
- `孤海注释` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
