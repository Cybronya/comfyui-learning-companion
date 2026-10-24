---
name: text_to_image_video_lora_sampler_23
type: Text To Image
frequency: 23
level: strong
coverage: 0.687435
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3+Viggle动作迁移强化版｜免提示词 数字人动作跟随超自然_2105512132791066626.json, 视频生成/图生视频/H3全能参考短剧工作流 多模态输入视频生成_2109027495902277633.json, 视频生成/图生视频/H3加Viggle免提示词动作迁移 人物视频动态强化版_2110357557851287554.json, 视频生成/图生视频/H3加Viggle免提示词动作迁移强化版，数字人视频生视频图生视频工具_2105724742098571266.json, 视频生成/图生视频/H3加Viggle免提示词动作迁移画质强化版，视频生视频图生视频工具_2105771049332858882.json, 视频生成/图生视频/H3官流最强武戏 视频生成官方最佳方案稳定出片_2109173230555713537.json, 视频生成/图生视频/H3官流终极版工作流，文生视频图生视频全覆盖方案_2109435565342019586.json, 视频生成/图生视频/H3工作流最优解 图生视频高质量稳定直出方案_2110367340926955522.json, 视频生成/图生视频/H3工作流最优解 视频生成最佳方案高效出片_2105350475045498881.json, 视频生成/图生视频/H3无损融合单采V2 官方满血API画布级本地流_2110225226482151425.json, 视频生成/图生视频/H3无损融合单采V2 官方满血API画布级本地流_2110353804985196545.json, 视频生成/图生视频/H3无损融合单采官方满血API画布级本地流 视频生成优化_2109397447813455873.json, 视频生成/图生视频/H3无损融合单采官方满血API画布级本地流 视频生成优化_2109781427771498497.json, 视频生成/图生视频/H3无损融合单采方案，速度俱佳图生视频出片_2111278197022224385.json, 视频生成/图生视频/H3无损融合单采满血API，画布级本地文生视频流_2111200196137934849.json, 视频生成/图生视频/H3最强单采V2雷霆祭祀版，33步战斗特效文生视频_2111228248330952705.json, 视频生成/图生视频/H3画布级本地流无损融合 官方满血API单采方案_2110351795410259970.json, 视频生成/图生视频/H3超级打戏无损工作流｜战斗特效分镜出图图生视频_2110709132494991362.json, 视频生成/图生视频/H3长视频衔接尾帧22帧锚点 视频生成连贯性优化_2109025859695890434.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim多帧动态优化_2110252157650956290.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim多帧动态优化_2110367355523133442.json, 视频生成/图生视频/Minimax H3完美人物替换 图生视频换人方案_2110363954835976194.json, 视频生成/图生视频/minimax-H3加Viggle动作迁移强化版，免提示词直接出片_2110451947428995074.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/H3+Viggle动作迁移强化版｜免提示词 数字人动作跟随超自然_2105512132791066626.json、视频生成/图生视频/H3全能参考短剧工作流 多模态输入视频生成_2109027495902277633.json、视频生成/图生视频/H3加Viggle免提示词动作迁移 人物视频动态强化版_2110357557851287554.json、视频生成/图生视频/H3加Viggle免提示词动作迁移强化版，数字人视频生视频图生视频工具_2105724742098571266.json、视频生成/图生视频/H3加Viggle免提示词动作迁移画质强化版，视频生视频图生视频工具_2105771049332858882.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 23 个 workflow 都包含：
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
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 22/23 个有
- `ModelPreviewOverrideKJ` —— 21/23 个有
- `SaveImage` —— 21/23 个有
- `PrimitiveFloat` —— 20/23 个有
- `VHS_LoadVideo` —— 20/23 个有
- `GetNode` —— 18/23 个有
- `ResolutionSelector` —— 18/23 个有
- `SetNode` —— 18/23 个有
- `VAEDecodeAudio` —— 18/23 个有
- `BlockSparseAttention` —— 16/23 个有
- `LoadAudio` —— 16/23 个有
- `MiniMaxH3ReferenceToVideo` —— 16/23 个有
- `PrimitiveStringMultiline` —— 16/23 个有
- `ManualSigmas` —— 13/23 个有
- `MiniMaxH3SigmaShift` —— 7/23 个有
- `CR Prompt Text` —— 5/23 个有
- `JWImageResizeToMegapixels` —— 5/23 个有
- `PreviewAny` —— 5/23 个有
- `ViggleAnimateConditioning` —— 5/23 个有
- `ViggleTextCondLoader` —— 5/23 个有
- `CR Value` —— 3/23 个有
- `MiniMaxH3AddGuide` —— 3/23 个有
- `RH_LLMAPI_Pro_Node` —— 3/23 个有
- `Fast Groups Bypasser (rgthree)` —— 2/23 个有
- `MiniMaxChunkFeedForward` —— 2/23 个有
- `MiniMaxH3ImageToVideo` —— 2/23 个有
- `MiniMaxLowVRAMAttention` —— 2/23 个有
- `GetImageRangeFromBatch` —— 1/23 个有
- `PreviewImage` —— 1/23 个有
- `TrimAudioDuration` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| 宽度 | 80 | 80 - 80 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高发问题（24/23 个样本）：Steps较低可能导致细节不足
