---
name: text_to_image_lora_sampler_clip_84
type: Text To Image
frequency: 15
level: strong
coverage: 0.901267
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/minimax h3长视频人物替换加动作迁移，内部循环视频生视频_2111516810670600194.json, 视频生成/图生视频/Minimax H3加速双采self-lift流｜两次采样提质量，速度还不打折_2099494675802583042.json, 视频生成/图生视频/Minimax H3加速双采｜self-lift工作流高效出片_2101155630626201602.json, 视频生成/图生视频/Minimax H3多参视频生成不油不偏色及一致性好工作流，图生视频处理方案_2107954357282099202.json, 视频生成/图生视频/Minimax h3多参视频生成不油不偏色及一致性好 多模态输入_2109712427955871745.json, 视频生成/图生视频/Minimax-H3开源加速双采工作流｜self-lift图生视频生成_2097766070177320962.json, 视频生成/图生视频/Minimax-H3开源黑科技加速双采｜self-lift图生视频战斗特效_2097917181681029122.json, 视频生成/图生视频/绘影MiniMax H3参考生视频self-lift双采1080P，混合25-49模型加速方案_2103171255007531010.json, 视频生成/图生视频/绘影出品｜Minimax H3参考生视频self-lift双采1080P高清V1版_2103018117453672449.json, 视频生成/图生视频/黑科技self-lift双采加速｜高动态画面表现力惊人_2103101451823308801.json, 视频生成/图生视频/黑科技加速双采SelfLift Heng图生视频处理工作流_2101779733385146370.json, 视频生成/图生视频/黑科技加速双采self-lift图生视频｜Minimax-H3开源战斗特效版_2097956772765069313.json, 视频生成/文生视频/Aiden黑科技加速双采self-lift工作流｜文图视频三模生视频_2097969163804438530.json, 视频生成/文生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099944178082992130.json, 视频生成/文生视频/H3黑科技加速加星光2.6高清放大融合工作流_2100311534835691522.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（数字人/数字人/minimax h3长视频人物替换加动作迁移，内部循环视频生视频_2111516810670600194.json、视频生成/图生视频/Minimax H3加速双采self-lift流｜两次采样提质量，速度还不打折_2099494675802583042.json、视频生成/图生视频/Minimax H3加速双采｜self-lift工作流高效出片_2101155630626201602.json、视频生成/图生视频/Minimax H3多参视频生成不油不偏色及一致性好工作流，图生视频处理方案_2107954357282099202.json、视频生成/图生视频/Minimax h3多参视频生成不油不偏色及一致性好 多模态输入_2109712427955871745.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 14/15 个有
- `MiniMaxH3ReferenceToVideo` —— 14/15 个有
- `PrimitiveFloat` —— 14/15 个有
- `SelfLiftH3Sampler` —— 14/15 个有
- `VAEDecodeAudio` —— 14/15 个有
- `CreateVideo` —— 11/15 个有
- `VHS_VideoCombine` —— 11/15 个有
- `SaveImage` —— 7/15 个有
- `SaveVideo` —— 5/15 个有
- `LoadAudio` —— 4/15 个有
- `MiniMaxH3SigmaShift` —— 3/15 个有
- `easy cleanGpuUsed` —— 2/15 个有
- `ImageConcatMulti` —— 1/15 个有
- `JWInteger` —— 1/15 个有
- `LoraLoaderBypassModelOnly` —— 1/15 个有
- `MiniMaxH3LongVideoSampler-solarL` —— 1/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/15 个有
- `PreviewAny` —— 1/15 个有
- `PrimitiveBoolean` —— 1/15 个有
- `RH_Astra` —— 1/15 个有
- `SaveVideoNode` —— 1/15 个有
- `VHS_LoadVideo` —— 1/15 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 1/15 个有
- `easy float` —— 1/15 个有
- `easy int` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
