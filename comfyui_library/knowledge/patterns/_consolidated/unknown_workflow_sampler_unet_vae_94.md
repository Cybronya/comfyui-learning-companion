---
name: unknown_workflow_sampler_unet_vae_94
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.94675
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Edit-2511文生图3D国漫CG风格_2079515568432046082.json, 图片生成/文生图/Qwen2.1文生图_2101145781234397185.json, 图片生成/文生图/Qwen_Edit_2509手机上的3D城市_2082741081346764801.json, 图片生成/文生图/Qwen_Edit_3D城市3D微景观_2011800399782617090.json, 图片生成/文生图/qwen image 2512 文生图_2091417972459008001.json, 图片生成/文生图/动作编辑器应用之四__FireRed文生图_2021382520541028354.json, 视频生成/图生视频/1982020667237384193.json, 视频生成/图生视频/1961983511181856769.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_94

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Qwen-Edit-2511文生图3D国漫CG风格_2079515568432046082.json、图片生成/文生图/Qwen2.1文生图_2101145781234397185.json、图片生成/文生图/Qwen_Edit_2509手机上的3D城市_2082741081346764801.json、图片生成/文生图/Qwen_Edit_3D城市3D微景观_2011800399782617090.json、图片生成/文生图/qwen image 2512 文生图_2091417972459008001.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `TextEncodeQwenImageEditPlus` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 6/8 个有
- `CFGNorm` —— 5/8 个有
- `LoadImage` —— 3/8 个有
- `TextEncodeQwenImageEdit` —— 2/8 个有
- `CR Latent Input Switch` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1280 | 8 | 83% |
| 高度 | 1152 | 720 - 1920 | 8 | 69% |
| 采样步数 | 4 | 4 - 25 | 8 | 3% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1280，8 个样本，取值集中（一致性 83%）
- 高度 中位数 1152，观测区间 720 - 1920，8 个样本
- 采样步数 中位数 4，观测区间 4 - 25，8 个样本，取值分散，一致性仅 3%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
