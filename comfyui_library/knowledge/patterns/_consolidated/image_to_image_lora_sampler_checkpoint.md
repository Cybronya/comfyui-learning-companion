---
name: image_to_image_lora_sampler_checkpoint
type: Image To Image
frequency: 25
level: strong
coverage: 0.81512
common_nodes: [CFGNorm, CLIPLoader, CheckpointLoaderSimple, ConditioningZeroOut, EmptySD3LatentImage, GetNode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SDPoseOODLoader, SDPoseOODProcessor, SaveImage, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, YOLOModelLoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王008、LH-电商换装_2034562991475138562.json, 图片生成/图生图/4K 4K Outfit Transfer + Pose Transfer 换装迁移 +姿态迁移+人_2102556522755743746.json, 图片生成/图生图/4K 4K Outfit Transfer + Pose Transfer 换装迁移 +姿态迁移+人_2102952594409869314.json, 图片生成/图生图/4K直出电商模特 换装_换人 万能迁移（服装 +姿态 +人物角色）超强人物一致性精准还原_2080450784256417794.json, 图片生成/图生图/4K直出电商模特_换装_换人_万能迁移服装_+姿态_+人物角色超强人物一致性精准还原_2085262641601269761.json, 图片生成/图生图/4K直出电商模特_换装_换人_万能迁移服装_+姿态_+人物角色超强人物一致性精准还原_2085689844143050754.json, 图片生成/图生图/4K直出电商模特_换装_换人_万能迁移服装_+姿态_+人物角色超强人物一致性精准还原_2085690907009052674.json, 图片生成/图生图/4K直出电商模特_换装_换人_万能迁移服装_+姿态_+人物角色超强人物一致性精准还原_2092606121411432450.json, 图片生成/图生图/4K直出电商模特换装迁移+姿态迁移+人物迁移超强人物一致性精准还原_2095687153224343553.json, 图片生成/图生图/4K直出电商模特换装迁移+姿态迁移+人物迁移超强人物一致性精准还原_2095695330825297922.json, 图片生成/图生图/4K直出电商模特（换装迁yi+姿态迁yi+人物迁yi）超强人物一致性精准还原_2045757205693075458.json, 图片生成/图生图/Posture Control4K Outfit Transfer Pose   换装迁移 姿态迁移_2107627479518240770.json, 图片生成/图生图/Posture Transfer Change Clothes换装迁移++姿态迁移_2104367502217277441.json, 图片生成/图生图/Q王炸-服装更换+姿势迁移+人像精修_2028739263361191937.json, 图片生成/图生图/加4K电商模特（换装迁yi+姿态迁yi+人物迁yi）超强人物一致性精准还原_2060615063458893826.json, 图片生成/图生图/实测最好用的开源电商换装工作流_2055205325011202050.json, 图片生成/图生图/换装（换装迁移+姿态迁移+人物迁移）超强人物一致性精准还原_2045336152353284098.json, 图片生成/图生图/服装姿态迁移-精准还原（qwen edit）_1996910703942516738.json, 平台全量/11.服装姿态迁移-精准还原+qwen+edit+++人物角色一致性+动作迁移+电商模_2000793137691979777.json, 平台全量/4K直出电商模特_换装_换人_万能迁移服装_+姿态_+人物角色超强人物一致性精准还原_2080859800593850370.json, 平台全量/4K直出电商模特_换装_换人_万能迁移服装_+姿态_+人物角色超强人物一致性精准还原_2080862975010889729.json, 平台全量/Qwen  edit 内附图集服装更换+姿势迁移+人像精修  高质量洗图  高清放大 自动反推提示词_2029722748313935873.json, 平台全量/换装+动作迁移 qwen 人物一致 平替Seedream 4.5  全能图片V1 Pro2.0_2003352801348550657.json, 平台全量/服装姿态迁移-精准还原 qwen edit   人物角色一致性 动作迁移 电商模_1999670192219226114.json, 平台全量/电商模特（服装迁移+姿态迁移+人物迁移）超强人物一致性精准还原_2000143905360408578.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王008、LH-电商换装_2034562991475138562.json、图片生成/图生图/4K 4K Outfit Transfer + Pose Transfer 换装迁移 +姿态迁移+人_2102556522755743746.json、图片生成/图生图/4K 4K Outfit Transfer + Pose Transfer 换装迁移 +姿态迁移+人_2102952594409869314.json、图片生成/图生图/4K直出电商模特 换装_换人 万能迁移（服装 +姿态 +人物角色）超强人物一致性精准还原_2080450784256417794.json、图片生成/图生图/4K直出电商模特_换装_换人_万能迁移服装_+姿态_+人物角色超强人物一致性精准还原_2085262641601269761.json…）

- **类型**：Image To Image
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 25 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `GroundingDinoModelLoader_SDPose` —— 21/25 个有
- `CR Text` —— 15/25 个有
- `INTConstant` —— 15/25 个有
- `ImageScaleToTotalPixels` —— 15/25 个有
- `MemoryCleaner` —— 15/25 个有
- `SeedVR2LoadDiTModel` —— 15/25 个有
- `SeedVR2LoadVAEModel` —— 15/25 个有
- `SeedVR2VideoUpscaler` —— 15/25 个有
- `Fast Groups Bypasser (rgthree)` —— 5/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 25 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 25 | 100% |
| 采样算法 | euler | - | 25 | 76% |
| 调度器 | simple | - | 25 | 76% |
| 重绘幅度 | 1 | 1 - 1 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 50/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，25 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，25 个样本，一致性 76%
- 调度器 最常用 simple，25 个样本，一致性 76%
- 重绘幅度 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 高发问题（50/25 个样本）：Steps较低可能导致细节不足
