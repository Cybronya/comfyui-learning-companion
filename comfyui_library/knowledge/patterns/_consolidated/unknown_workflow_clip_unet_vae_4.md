---
name: unknown_workflow_clip_unet_vae_4
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.931778
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图_1999752689116475393.json, 图片生成/文生图/文生图_2018496192077897730.json, 图片生成/文生图/文生图_2067423263386591234.json, 图片生成/文生图/文生图大模型DeepSeek时刻！Z-Image宣判封顶！家用显卡就能运行！_1995826953766723586.json, 图片生成/文生图/（老白lokr版-贞贞124500步）Z-Image-Base文生图V1(还没拟合。。)_2019370836720885761.json, 图片生成/文生图/（老白lokr版-贞贞145000步）Z-Image-Base文生图V1(还模型到底还能拟合吗？)_2019682330843025410.json, 图片生成/文生图/（老白lokr版-贞贞165000步）Z-Image-Base文生图V1(这模型到底还能拟合吗？)_2020080899903197186.json, 图片生成/文生图/（老白lokr版-贞贞8W4）Z-Image-Base文生图V1(还没拟合。。)_2018764663516831745.json, 图片生成/文生图/（贞贞版3W步绝美版）Z-Image-Base文生图V1_2016831860403343362.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/文生图_1999752689116475393.json、图片生成/文生图/文生图_2018496192077897730.json、图片生成/文生图/文生图_2067423263386591234.json、图片生成/文生图/文生图大模型DeepSeek时刻！Z-Image宣判封顶！家用显卡就能运行！_1995826953766723586.json、图片生成/文生图/（老白lokr版-贞贞124500步）Z-Image-Base文生图V1(还没拟合。。)_2019370836720885761.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 8/9 个有
- `LoadImage` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `LayerUtility: PurgeVRAM` —— 5/9 个有
- `JWFloat` —— 4/9 个有
- `ConditioningZeroOut` —— 2/9 个有
- `KSamplerAdvanced` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `VAEEncode` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 9 - 50 | 8 | 57% |
| Prompt 约束强度(CFG) | 4 | 1 - 10 | 9 | 37% |
| 采样算法 | res_multistep | - | 9 | 56% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 50，观测区间 9 - 50，8 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 10，9 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 res_multistep，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
