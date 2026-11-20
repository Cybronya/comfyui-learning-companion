---
name: text_to_image_lora_sampler_clip_81
type: Text To Image
frequency: 15
level: strong
coverage: 0.83
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/动作迁移生成视频工作流 MiniMax H3 FL2VA开源版人物模仿方案_2094028776626810881.json, 视频生成/图生视频/动作迁移生成视频工作流 MiniMax H3 FL2VA开源版人物模仿方案_2097108484516044801.json, 视频生成/图生视频/动作迁移生成视频工作流 MiniMax H3 FL2VA开源版人物模仿方案_2098919542293614593.json, 视频生成/图生视频/动作迁移生成视频工作流 MiniMax H3 FL2VA开源版人物模仿方案_2110198601912766465.json, 视频生成/图生视频/动作迁移生成视频｜MiniMax H3 FL2VA开源版工作流_2093545405677133826.json, 视频生成/图生视频/动作迁移生成视频｜MiniMax H3 FL2VA开源版工作流_2093855259834806274.json, 视频生成/图生视频/单图生成视频｜MiniMax H3 FL2VA开源版工作流_2093251838228393985.json, 视频生成/图生视频/单图生成视频｜MiniMax H3 FL2VA开源版工作流_2094055607228780545.json, 视频生成/图生视频/单图生成视频｜MiniMax H3 FL2VA开源版直出_2093852526583050241.json, 视频生成/图生视频/去高动态噪点加速版｜Minimax H3图生视频首尾帧高清出片_2088736756886757378.json, 视频生成/图生视频/图生视频轻松上手｜MiniMax H3 基础款快速出片_2096251513273405442.json, 视频生成/图生视频/漫剧林辰图生视频｜短剧角色动起来 图生视频一键成片_2104102680842039298.json, 视频生成/视频生视频/MiniMax H3 FL2VA开源版 用动作迁移直接生成视频_2106528532062101505.json, 视频生成/视频生视频/MiniMax H3 FL2VA开源版工作流 视频动作迁移人物图生视频方案_2106171693709488129.json, 视频生成/视频生视频/动作迁移生成视频工作流 MiniMax H3 FL2VA开源版人物模仿方案_2106167033271508993.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/动作迁移生成视频工作流 MiniMax H3 FL2VA开源版人物模仿方案_2094028776626810881.json、视频生成/图生视频/动作迁移生成视频工作流 MiniMax H3 FL2VA开源版人物模仿方案_2097108484516044801.json、视频生成/图生视频/动作迁移生成视频工作流 MiniMax H3 FL2VA开源版人物模仿方案_2098919542293614593.json、视频生成/图生视频/动作迁移生成视频工作流 MiniMax H3 FL2VA开源版人物模仿方案_2110198601912766465.json、视频生成/图生视频/动作迁移生成视频｜MiniMax H3 FL2VA开源版工作流_2093545405677133826.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 14/15 个有
- `孤海注释` —— 14/15 个有
- `ComfySwitchNode` —— 13/15 个有
- `ImageScale` —— 13/15 个有
- `PrimitiveBoolean` —— 13/15 个有
- `PrimitiveInt` —— 13/15 个有
- `MiniMaxH3ReferenceToVideo` —— 10/15 个有
- `GetVideoComponents` —— 9/15 个有
- `LoadVideo` —— 9/15 个有
- `Video Slice` —— 9/15 个有
- `VideoFrameSample` —— 9/15 个有
- `VAEDecodeAudio` —— 6/15 个有
- `MiniMaxH3ImageToVideo` —— 5/15 个有
- `CR Text` —— 4/15 个有
- `ResolutionSelector` —— 3/15 个有
- `ImageScaleToTotalPixels` —— 2/15 个有
- `PathchSageAttentionKJ` —— 2/15 个有
- `ExtendIntermediateSigmas` —— 1/15 个有
- `H3SigmaRefiner` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `LayerUtility: TextBox` —— 1/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
