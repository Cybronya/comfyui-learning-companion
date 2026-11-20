---
name: text_to_image_video_lora_sampler_16
type: Text To Image
frequency: 27
level: strong
coverage: 0.687037
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3+Viggle动作迁移强化版｜免提示词 数字人动作跟随超自然_2105512132791066626.json, 视频生成/图生视频/H3全能参考短剧工作流 多模态输入视频生成_2109027495902277633.json, 视频生成/图生视频/H3加Viggle免提示词动作迁移 人物视频动态强化版_2110357557851287554.json, 视频生成/图生视频/H3加Viggle免提示词动作迁移强化版，数字人视频生视频图生视频工具_2105724742098571266.json, 视频生成/图生视频/H3加Viggle免提示词动作迁移画质强化版，视频生视频图生视频工具_2105771049332858882.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107218917725917186.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107335317010345985.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107445931183534081.json, 视频生成/图生视频/H3单采极速文戏工作流，图生视频高效创作方案_2107957288756666370.json, 视频生成/图生视频/H3单采极速文戏工作流｜图生视频高效创作首选方案_2107667535738007554.json, 视频生成/图生视频/H3单采极速文戏流程，图生视频快速产出高质量片段_2110496089349640194.json, 视频生成/图生视频/H3单采极速文戏，图生视频快速产出高质量片段_2110827618437255169.json, 视频生成/图生视频/H3无损融合单采10步手动挡 斗气增强战斗特效处理工具_2113010568260046850.json, 视频生成/图生视频/H3无损融合单采V2 官方满血API画布级本地流_2110225226482151425.json, 视频生成/图生视频/H3无损融合单采V2 官方满血API画布级本地流_2110353804985196545.json, 视频生成/图生视频/H3无损融合单采官方满血API画布级本地流 视频生成优化_2109397447813455873.json, 视频生成/图生视频/H3无损融合单采官方满血API画布级本地流 视频生成优化_2109781427771498497.json, 视频生成/图生视频/H3无损融合单采方案，速度俱佳图生视频出片_2111278197022224385.json, 视频生成/图生视频/H3无损融合单采满血API，画布级本地文生视频流_2111200196137934849.json, 视频生成/图生视频/H3最强单采8步Lora 动作迁移角色替换视频生成工具_2113692337875546114.json, 视频生成/图生视频/H3最强单采8步lora加换角色lora｜动作迁移角色替换上限更高进阶版_2113445708056584194.json, 视频生成/图生视频/H3最强单采V2雷霆祭祀版，33步战斗特效文生视频_2111228248330952705.json, 视频生成/图生视频/H3画布级本地流无损融合 官方满血API单采方案_2110351795410259970.json, 视频生成/图生视频/H3超级打戏无损工作流｜战斗特效分镜出图图生视频_2110709132494991362.json, 视频生成/图生视频/H3长视频衔接尾帧22帧锚点 视频生成连贯性优化_2109025859695890434.json, 视频生成/图生视频/minimax-H3加Viggle动作迁移强化版，免提示词直接出片_2110451947428995074.json, 视频生成/图生视频/minimax-H3加Viggle动作迁移强化版，免提示词直接出片_2113808831812816898.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/H3+Viggle动作迁移强化版｜免提示词 数字人动作跟随超自然_2105512132791066626.json、视频生成/图生视频/H3全能参考短剧工作流 多模态输入视频生成_2109027495902277633.json、视频生成/图生视频/H3加Viggle免提示词动作迁移 人物视频动态强化版_2110357557851287554.json、视频生成/图生视频/H3加Viggle免提示词动作迁移强化版，数字人视频生视频图生视频工具_2105724742098571266.json、视频生成/图生视频/H3加Viggle免提示词动作迁移画质强化版，视频生视频图生视频工具_2105771049332858882.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 27 个 workflow 都包含：
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
- `VHS_LoadVideo` —— 26/27 个有
- `SaveImage` —— 24/27 个有
- `孤海注释` —— 24/27 个有
- `PrimitiveFloat` —— 23/27 个有
- `LoadAudio` —— 21/27 个有
- `MiniMaxH3ReferenceToVideo` —— 21/27 个有
- `ResolutionSelector` —— 21/27 个有
- `VAEDecodeAudio` —— 21/27 个有
- `GetNode` —— 20/27 个有
- `ModelPreviewOverrideKJ` —— 20/27 个有
- `SetNode` —— 20/27 个有
- `BlockSparseAttention` —— 19/27 个有
- `PrimitiveStringMultiline` —— 19/27 个有
- `MiniMaxH3SigmaShift` —— 13/27 个有
- `ManualSigmas` —— 9/27 个有
- `EmptyImage` —— 7/27 个有
- `ExtendIntermediateSigmas` —— 7/27 个有
- `PreviewAny` —— 7/27 个有
- `PreviewImage` —— 7/27 个有
- `JWImageResizeToMegapixels` —— 6/27 个有
- `ViggleAnimateConditioning` —— 6/27 个有
- `ViggleTextCondLoader` —— 6/27 个有
- `CR Value` —— 4/27 个有
- `CR Prompt Text` —— 2/27 个有
- `Fast Groups Bypasser (rgthree)` —— 2/27 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/27 个有
- `MiniMaxChunkFeedForward` —— 2/27 个有
- `MiniMaxLowVRAMAttention` —— 2/27 个有
- `GetImageRangeFromBatch` —— 1/27 个有
- `MiniMaxH3AddGuide` —— 1/27 个有
- `TrimAudioDuration` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |
| 高度 | 80 | 80 - 80 | 27 | 100% |
| 采样算法 | er_sde | - | 27 | 100% |
| 调度器 | beta | - | 27 | 100% |
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| 宽度 | 80 | 80 - 80 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，27 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，27 个样本，一致性 100%
- 调度器 最常用 beta，27 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高发问题（31/27 个样本）：Steps较低可能导致细节不足
