---
name: text_to_image_lora_sampler_clip_12
type: Text To Image
frequency: 29
level: strong
coverage: 0.726759
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/人物替换单人稳定版｜Minimax H3图生视频工作流_2087216847925104641.json, 视频生成/图生视频/人物替换智能反推｜Minimax H3 角色一致动作迁移图生视频_2089265425245892609.json, 视频生成/图生视频/人物替换角色一致性｜Minimax H3智能反推免手写图生视频_2091251915622539266.json, 视频生成/图生视频/免手写提示词 MiniMax H3角色一致性图生视频人物替换_2095075157848182785.json, 视频生成/图生视频/免手写提示词 MiniMax H3角色一致性图生视频人物替换_2097468927143141377.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2089305534913667073.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3 自定义背景人物动作迁移_2090649252212076545.json, 视频生成/图生视频/全能参考生视频｜MiniMax H3自定义背景人物迁移_2090938897554567170.json, 视频生成/图生视频/动作迁移单人稳定版｜Minimax H3图生视频工作流_2087226692820619265.json, 视频生成/图生视频/动作迁移单人稳定版｜Minimax H3图生视频工作流_2092982995232845825.json, 视频生成/图生视频/图生视频工作流Minimax H3单人稳定版动作迁移高效首选_2089319411319664642.json, 视频生成/图生视频/图生视频工作流Minimax H3单人稳定版动作迁移高效首选_2091760129564831746.json, 视频生成/图生视频/智能反推免手写｜Minimax H3人物替换角色一致性图生视频_2093989857021485058.json, 视频生成/图生视频/智能反推提示词 Minimax H3人物替换更省心_2097826550262620161.json, 视频生成/图生视频/智能反推提示词 Minimax H3人物替换更省心_2099639194716033025.json, 视频生成/图生视频/智能反推提示词_Minimax_H3人物替换更省心_2109101235495325697.json, 视频生成/图生视频/智能反推提示词人物替换｜MiniMax H3图生视频_2093459389402411009.json, 视频生成/图生视频/智能反推提示词免手写 Minimax H3角色一致性人物替换图生视频方案_2094019678422265857.json, 视频生成/图生视频/智能反推提示词免手写 Minimax H3角色一致性人物替换图生视频方案_2097098707203346434.json, 视频生成/图生视频/自定义背景人物全能参考 MiniMax H3动作迁移图生视频工作流_2089320676988637185.json, 视频生成/图生视频/自定义背景人物参考｜MiniMax H3动作迁移图生视频_2093084247081963522.json, 视频生成/图生视频/角色一致动作迁移人物替换｜H3智能反推提示词图生视频_2092363921817686017.json, 视频生成/图生视频/角色一致动作迁移｜MiniMax H3人物替换智能反推方案_2093472951667609602.json, 视频生成/图生视频/角色一致动作迁移｜Minimax H3人物替换智能反推图生视频_2089457405968076801.json, 视频生成/图生视频/角色一致动作迁移｜Minimax H3人物替换智能反推图生视频_2091250634946334721.json, 视频生成/图生视频/角色一致动作迁移｜Minimax H3智能反推人物替换_2090884451969622017.json, 视频生成/文生视频/H3全能参考生视频MiniMax视频生视频图生视频_2086209628857266177.json, 视频生成/视频生视频/免手写提示词 MiniMax H3角色一致性图生视频人物替换_2106531233084821505.json, 视频生成/视频生视频/智能反推提示词免手写 Minimax H3角色一致性人物替换图生视频方案_2106158187798941698.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_12

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/图生视频/人物替换单人稳定版｜Minimax H3图生视频工作流_2087216847925104641.json、视频生成/图生视频/人物替换智能反推｜Minimax H3 角色一致动作迁移图生视频_2089265425245892609.json、视频生成/图生视频/人物替换角色一致性｜Minimax H3智能反推免手写图生视频_2091251915622539266.json、视频生成/图生视频/免手写提示词 MiniMax H3角色一致性图生视频人物替换_2095075157848182785.json、视频生成/图生视频/免手写提示词 MiniMax H3角色一致性图生视频人物替换_2097468927143141377.json…）

- **类型**：Text To Image
- **样本数**：29
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 29 个 workflow 都包含：
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 28/29 个有
- `孤海注释` —— 25/29 个有
- `EasyCache` —— 24/29 个有
- `Fast Groups Bypasser (rgthree)` —— 24/29 个有
- `GetNode` —— 24/29 个有
- `PrimitiveFloat` —— 24/29 个有
- `SetNode` —— 24/29 个有
- `easy showAnything` —— 23/29 个有
- `PrimitiveInt` —— 18/29 个有
- `RHHiddenNodes` —— 18/29 个有
- `CR Prompt Text` —— 6/29 个有
- `Bjornulf_ShowFloat` —— 5/29 个有
- `JoinStrings` —— 5/29 个有
- `LoadAudio` —— 5/29 个有
- `PrimitiveStringMultiline` —— 5/29 个有
- `RH_LLMAPI_Pro_Node` —— 5/29 个有
- `VHS_VideoInfoLoaded` —— 5/29 个有
- `LoadVideo` —— 4/29 个有
- `EmptyImage` —— 1/29 个有
- `PreviewImage` —— 1/29 个有
- `VideoFrameSelector` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 29 | 100% |
| 高度 | 80 | 80 - 80 | 29 | 100% |
| 采样步数 | 4 | 4 - 4 | 29 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 29 | 100% |
| 采样算法 | er_sde | - | 29 | 100% |
| 调度器 | beta | - | 29 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 36/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，29 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，29 个样本，一致性 100%
- 调度器 最常用 beta，29 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 高发问题（36/29 个样本）：Steps较低可能导致细节不足
