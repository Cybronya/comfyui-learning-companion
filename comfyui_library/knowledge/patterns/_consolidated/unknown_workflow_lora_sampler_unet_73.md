---
name: unknown_workflow_lora_sampler_unet_73
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.921444
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/01qsyimage_2048154773131628545.json, 图片生成/反推提示词/1dvcunxuswp_2059681852159516674.json, 图片生成/反推提示词/1famtkmmjca_2060260787788275714.json, 图片生成/反推提示词/2343244_2046154948538273793.json, 图片生成/反推提示词/31itoi3h1_2049743007620055041.json, 图片生成/反推提示词/xwnst425_2047929562071306241.json, 图片生成/反推提示词/溶图tst343244_2046156838932058114.json, 平台全量/Qwen-Eidt-2511三图参考_2064272496332988417.json, 平台全量/tstmikezhang_2046823338646970370.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_73

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/01qsyimage_2048154773131628545.json、图片生成/反推提示词/1dvcunxuswp_2059681852159516674.json、图片生成/反推提示词/1famtkmmjca_2060260787788275714.json、图片生成/反推提示词/2343244_2046154948538273793.json、图片生成/反推提示词/31itoi3h1_2049743007620055041.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 8/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 8/9 个有
- `RTXVideoSuperResolution` —— 7/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `CFGNorm` —— 4/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `Fast Groups Muter (rgthree)` —— 4/9 个有
- `ModelSamplingAuraFlow` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `ShellAgentPluginOutputText` —— 2/9 个有
- `Image Comparer (rgthree)` —— 1/9 个有
- `Int` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 9 | 66% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 720 | 400 - 1024 | 9 | 74% |
| 高度 | 1080 | 744 - 1536 | 9 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 720，观测区间 400 - 1024，9 个样本
- 高度 中位数 1080，观测区间 744 - 1536，9 个样本
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
