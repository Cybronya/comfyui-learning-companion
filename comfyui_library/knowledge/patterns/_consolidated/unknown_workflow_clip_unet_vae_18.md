---
name: unknown_workflow_clip_unet_vae_18
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.466333
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, ConditioningZeroOut, GetNode, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1FINAL-文生图_2049358468934541313.json, 图片生成/文生图/qwen + z-image + qwen2512 三合一批量文生图 亚马逊外国模特场景生成_2018887241812152322.json, 图片生成/文生图/图像反推-提示词-生图 Qwen大模型_2037005035095199745.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_18

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1FINAL-文生图_2049358468934541313.json、图片生成/文生图/qwen + z-image + qwen2512 三合一批量文生图 亚马逊外国模特场景生成_2018887241812152322.json、图片生成/文生图/图像反推-提示词-生图 Qwen大模型_2037005035095199745.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `ConditioningZeroOut`
- `GetNode`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `KSampler` —— 2/3 个有
- `KSamplerAdvanced` —— 2/3 个有
- `LatentColorMatch` —— 2/3 个有
- `LayerColor: Brightness & Contrast` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy seed` —— 2/3 个有
- `CR Prompt List` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 3 | 0% |
| 采样算法 | 1 | - | 3 | 33% |
| 调度器 | euler_ancestral | - | 3 | 33% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，3 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 1，3 个样本，一致性 33%
- 调度器 最常用 euler_ancestral，3 个样本，一致性 33%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
