---
name: text_to_image_lora_sampler_clip_192
type: Text To Image
frequency: 9
level: strong
coverage: 0.866444
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Minimax H3单人版人物替换｜自动反推提示词免手写｜一键视频换人_2112064275526279169.json, 图片生成/图生图/单人人物替换自动反推，Minimax H3动作迁移图生图_2112250764386193410.json, 图片生成/图生图/故事多分镜图处理｜Minimax h3高一致性出图_2093805215270129666.json, 图片生成/图生图/故事多分镜高一致性｜Minimax h3场景环境图处理_2094026676677210113.json, 数字人/数字人/9参考MINIMAX-H3数字人_2086538496143089666.json, 视频生成/图生视频/BUNNY_H3单采er_sde手动Sigma，文生视频节奏随心控_2110519304910364674.json, 视频生成/图生视频/H3高清快速出视频工作流，图生视频高效创作工具_2106126711132876801.json, 视频生成/图生视频/MiniMax H3角色替换｜单人指定角色+视频编辑多合一_2110716972131512322.json, 视频生成/图生视频/人物替换单人稳定版｜Minimax H3图生视频工作流_2087216847925104641.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_192

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Minimax H3单人版人物替换｜自动反推提示词免手写｜一键视频换人_2112064275526279169.json、图片生成/图生图/单人人物替换自动反推，Minimax H3动作迁移图生图_2112250764386193410.json、图片生成/图生图/故事多分镜图处理｜Minimax h3高一致性出图_2093805215270129666.json、图片生成/图生图/故事多分镜高一致性｜Minimax h3场景环境图处理_2094026676677210113.json、数字人/数字人/9参考MINIMAX-H3数字人_2086538496143089666.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 7/9 个有
- `CreateVideo` —— 7/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/9 个有
- `PrimitiveFloat` —— 6/9 个有
- `VHS_VideoCombine` —— 6/9 个有
- `ModelAttentionBackend` —— 5/9 个有
- `SaveImage` —— 5/9 个有
- `VHS_LoadVideo` —— 5/9 个有
- `JoinStrings` —— 4/9 个有
- `Bjornulf_ShowFloat` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 3/9 个有
- `LoadAudio` —— 3/9 个有
- `ManualSigmas` —— 3/9 个有
- `ModelPreviewOverrideKJ` —— 3/9 个有
- `RH_LLMAPI_Pro_Node` —— 3/9 个有
- `SaveVideo` —— 3/9 个有
- `VHS_VideoInfoLoaded` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `BlockSparseAttention` —— 2/9 个有
- `EasyCache` —— 2/9 个有
- `GetImagesFromBatchIndexed` —— 2/9 个有
- `GetVideoComponents` —— 2/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `JWString` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LoadVideo` —— 1/9 个有
- `LoraLoaderBypassModelOnly` —— 1/9 个有
- `MiniMaxH3SigmaShift` —— 1/9 个有
- `MiniMaxH3Unified` —— 1/9 个有
- `VideoFrameSelector` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
