---
name: text_to_image_video_lora_sampler_103
type: Text To Image
frequency: 7
level: strong
coverage: 0.877286
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3超写实数字人｜真假难分_2089545869266866177.json, 视频生成/图生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086425565711654914.json, 视频生成/图生视频/T6全参官方指南｜minimaxh3自动扩展提示词分镜出图_2094333256052334594.json, 视频生成/图生视频/T8全参官方指南｜minimaxh3扩展提示词角色一致性生视频_2094463893199482882.json, 视频生成/图生视频/minimaxH3 多参考视频PV工作流｜备用方案图生视频更稳妥_2097504953928605697.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词_2086537843907846146.json, 视频生成/图生视频/口播直出｜MinimaxH3数字人图生视频生成_2089809950645248002.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_103

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3超写实数字人｜真假难分_2089545869266866177.json、视频生成/图生视频/Minimax开源版H3多宫格图生视频开源版加速版_2086425565711654914.json、视频生成/图生视频/T6全参官方指南｜minimaxh3自动扩展提示词分镜出图_2094333256052334594.json、视频生成/图生视频/T8全参官方指南｜minimaxh3扩展提示词角色一致性生视频_2094463893199482882.json、视频生成/图生视频/minimaxH3 多参考视频PV工作流｜备用方案图生视频更稳妥_2097504953928605697.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `LoadAudio` —— 5/7 个有
- `VAEDecodeAudio` —— 5/7 个有
- `孤海注释` —— 5/7 个有
- `MiniMaxH3ReferenceToVideo` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `ImageConcatenateMulti_UTK` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `Text` —— 3/7 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 3/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `SaveAudio` —— 2/7 个有
- `TrimAudioDuration` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `ModelPreviewOverrideKJ` —— 1/7 个有
- `PainterVRAM` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有
- `TextConcatenate_UTK` —— 1/7 个有
- `VHS_SelectImages` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
