---
name: unknown_workflow_sampler_vae_22
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.989688
common_nodes: [EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Aio V18 单图编辑 +双图编辑 +三图编辑 系列合集_2005540173163233281.json, 图片生成/图生图/Qwen-Edit 2511 Aio V16侧视图编辑_2004423373528723457.json, 图片生成/图生图/Qwen-Edit 2511 Aio V16单图编辑 本地解码_2004493674581032961.json, 图片生成/图生图/Qwen-Edit 2511 Aio V16单图编辑_2004242718605930498.json, 图片生成/图生图/Qwen-Edit 2511 Aio V16单图编辑_2005517645359312898.json, 图片生成/图生图/Qwen-Edit 2511 Aio V18单图编辑_2005365205876043778.json, 图片生成/图生图/图片转换反推出图_2005475558886699010.json, 图片生成/图生图/服装模特姿势一键换姿势同步迁移动作_2066127241259606018.json, 图片生成/图生图/（自用）Qwen Edit 2511 Aio V16编辑V3（姿势迁移-sex tacular）_2004244864671907841.json, 图片生成/图生图/（自用）Qwen Edit 2511 Aio V18编辑V2（姿势迁移-sex tacular）_2004960067831169026.json, 图片生成/图生图/（自用）Qwen-Edit Aio V4模型双图编辑(姿势迁移)_1977756644379611138.json, 图片生成/图生图/（自用）Qwen-Edit Aio V5.1模型双图编辑(姿势迁移)_1980187956537364481.json, 图片生成/图生图/（自用）Qwen-Edit Aio V5.2模型双图编辑(姿势迁移)_1982145260451184641.json, 图片生成/图生图/（自用）Qwen-Edit Aio V5模型双图编辑(姿势迁移)_1978123448637644801.json, 图片生成/图生图/🦖Qwen Edit 2511姿势迁移(可本地解码)_2008042497682968578.json, 视频生成/图生视频/服装模特姿势一键换姿势同步迁移动作（懒人版）_2066565201717194754.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_22

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Qwen Aio V18 单图编辑 +双图编辑 +三图编辑 系列合集_2005540173163233281.json、图片生成/图生图/Qwen-Edit 2511 Aio V16侧视图编辑_2004423373528723457.json、图片生成/图生图/Qwen-Edit 2511 Aio V16单图编辑 本地解码_2004493674581032961.json、图片生成/图生图/Qwen-Edit 2511 Aio V16单图编辑_2004242718605930498.json、图片生成/图生图/Qwen-Edit 2511 Aio V16单图编辑_2005517645359312898.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 16 个 workflow 都包含：
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 15/16 个有
- `GetImageSizeAndCount` —— 15/16 个有
- `Text Multiline` —— 15/16 个有
- `CLIPLoader` —— 10/16 个有
- `ImageConcanate` —— 10/16 个有
- `CR Prompt Text` —— 9/16 个有
- `DWPreprocessor` —— 9/16 个有
- `TT_img_enc` —— 9/16 个有
- `VAELoader` —— 9/16 个有
- `LoraLoaderModelOnly` —— 8/16 个有
- `TT_img_enc_v2` —— 6/16 个有
- `DuckHideNode` —— 4/16 个有
- `UNETLoader` —— 4/16 个有
- `ImageConcatMulti` —— 2/16 个有
- `AddLabel` —— 1/16 个有
- `easy anythingIndexSwitch` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 10 | 16 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 38% |
| 调度器 | beta | - | 16 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 768 | 768 - 1024 | 16 | 92% |
| 高度 | 768 | 768 - 1920 | 16 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 10，16 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 38%
- 调度器 最常用 beta，16 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 1024，16 个样本，取值集中（一致性 92%）
- 高度 中位数 768，观测区间 768 - 1920，16 个样本
- 高发问题（24/16 个样本）：Steps较低可能导致细节不足
