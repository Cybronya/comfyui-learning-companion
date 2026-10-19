---
name: text_to_image_video_lora_sampler_11
type: Text To Image
frequency: 25
level: strong
coverage: 0.82212
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax-H3lora)ENG8步多参生视频(双时钟图生极速2分钟出5秒ENG_2087129153064751106.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜SLA脸部动作稳定版_2097906883771330562.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意生成_2094540734518091777.json, 视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意视频制作_2107673663351910401.json, 视频生成/图生视频/Minimax-H3潜空间放大一采版｜预览锁种稳定出片_2098748687479562242.json, 视频生成/图生视频/Minimax-H3电商宣传广告｜产品视频高质量生成_2095594718758531074.json, 视频生成/图生视频/Minimax海螺H3加速版｜图生视频8步高质量，极速出片_2099892617046740993.json, 视频生成/图生视频/Minimax海螺h3图生视频8步极速优化版t8｜高质量加速_2100809902179573761.json, 视频生成/图生视频/Remix双采加速参考生视频｜MiniMax-H3 Latent Upscaler_2093484648100884482.json, 视频生成/图生视频/SLA脸部动作稳定版｜Minimax-H3开源参考生视频角色一致_2091613796845572097.json, 视频生成/图生视频/SLA脸部动作稳定｜Minimax-H3参考生视频角色一致性_2091785773665316865.json, 视频生成/图生视频/Seedance2.5文生视频工作流｜视频运镜高质量生成_2097809713382649858.json, 视频生成/图生视频/minimax商品视频展示 产品展示动态效果一键生成_2104643850022252545.json, 视频生成/图生视频/minimax商品视频展示｜图生视频电商产品动态主图制作_2104552227313639426.json, 视频生成/图生视频/minmax生图工作流｜图生视频配套生图方案_2097990295555235841.json, 视频生成/图生视频/动态最强参考生视频｜MiniMax H3 V1版图生视频_2095050766850551809.json, 视频生成/图生视频/参考生视频最强战斗效果｜MiniMax H3多图参考图生视频_2096673588765093890.json, 视频生成/图生视频/双时钟双采加速｜Latent Upscaler参考生视频H3版_2092746811000844289.json, 视频生成/图生视频/双时钟双采加速｜Minimax H3 Latent Upscaler图生视频_2091203656212373506.json, 视频生成/图生视频/文戏短剧专用工作流｜MINIMAX-H3 图生视频细腻演绎_2096245265643692034.json, 视频生成/图生视频/最强Minimax商品视频展示工作流，图生视频电商产品展示处理工具_2108426664534433793.json, 视频生成/图生视频/格莱美慢镜头质感 MiniMax H3双采参考生视频动态可控_2104360820577759233.json, 视频生成/文生视频/9月30日目前最强武戏高动态 极速高清自动提示词加手动提示词2选1_2105345913706340354.json, 视频生成/文生视频/MiniMax H3高动文武双修工作流，文生视频视频生视频图生视频方案_2107167458216996865.json, 视频生成/文生视频/minimaxh3高动文武双修工作流 视频生成均衡方案_2108674482876534786.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3lora)ENG8步多参生视频(双时钟图生极速2分钟出5秒ENG_2087129153064751106.json、视频生成/图生视频/Minimax-H3开源参考生视频｜SLA脸部动作稳定版_2097906883771330562.json、视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意生成_2094540734518091777.json、视频生成/图生视频/Minimax-H3开源参考生视频｜短剧漫剧创意视频制作_2107673663351910401.json、视频生成/图生视频/Minimax-H3潜空间放大一采版｜预览锁种稳定出片_2098748687479562242.json…）

- **类型**：Text To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 23/25 个有
- `ModelAttentionBackend` —— 20/25 个有
- `SolAttnMiniMax` —— 18/25 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 15/25 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 15/25 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 15/25 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 15/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/25 个有
- `PreviewImage` —— 8/25 个有
- `SaveImage` —— 8/25 个有
- `ConcatTextOfUtils` —— 7/25 个有
- `Fast Groups Bypasser (rgthree)` —— 7/25 个有
- `GetNode` —— 7/25 个有
- `SetNode` —— 7/25 个有
- `Float` —— 5/25 个有
- `VAEDecodeAudio` —— 5/25 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 4/25 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 4/25 个有
- `PreviewAny` —— 3/25 个有
- `RH_LLMAPI_Pro_Node` —— 3/25 个有
- `LoadAudio` —— 2/25 个有
- `MiniMaxH3TurboLoRA` —— 2/25 个有
- `PrimitiveStringMultiline` —— 2/25 个有
- `Fast Groups Muter (rgthree)` —— 1/25 个有
- `Fast Muter (rgthree)` —— 1/25 个有
- `ImageCrop` —— 1/25 个有
- `ImageFromBatch` —— 1/25 个有
- `ImpactSwitch` —— 1/25 个有
- `PrimitiveInt` —— 1/25 个有
- `Seed (rgthree)` —— 1/25 个有
- `Text Multiline` —— 1/25 个有
- `TrimAudioDuration` —— 1/25 个有
- `VHS_LoadVideo` —— 1/25 个有
- `easy anythingIndexSwitch` —— 1/25 个有
- `easy cleanGpuUsed` —— 1/25 个有
- `忽略多组孤海` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 25 | 100% |
| 采样算法 | er_sde | - | 25 | 100% |
| 调度器 | beta | - | 25 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |
| 宽度 | 80 | 80 - 80 | 25 | 100% |
| 高度 | 80 | 80 - 80 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，25 个样本，一致性 100%
- 调度器 最常用 beta，25 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，25 个样本，取值集中（一致性 100%）
- 高发问题（25/25 个样本）：Steps较低可能导致细节不足
