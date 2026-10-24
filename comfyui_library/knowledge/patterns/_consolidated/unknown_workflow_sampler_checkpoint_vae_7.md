---
name: unknown_workflow_sampler_checkpoint_vae_7
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.983455
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王016.三图融合-精简_2034657573575598081.json, 图片生成/图生图/251223001-分镜一致性11.Qwen三图融合-NF_2003132198746300418.json, 图片生成/图生图/251224001.在线版Ps-Qwen-LHSTW30M-三图融合-NF_2003630969938714625.json, 图片生成/图生图/LH-DMT版本-2.生图片类-050.Qwen三图融合-NF_2016525076501368833.json, 图片生成/图生图/Qwen-Edit 2511 Aio V16单图编辑修改去水印等_2006632675330756610.json, 图片生成/图生图/Qwen-Edit 2511 Aio V18 多视图编辑_2004834515447148546.json, 图片生成/图生图/Qwen-Edit Aio V4模型单图编辑_1977759988884066305.json, 图片生成/图生图/Qwen-Edit Aio V5模型单图编辑2_1978126710321373185.json, 图片生成/图生图/Qwen-Edit Aio V7模型单图编辑2_1985325755531993090.json, 图片生成/图生图/Qwen-Edit Aio （姿势迁移）V20_1978746471015141377.json, 图片生成/图生图/V5模型（最新一致性姿势迁移）Qwen-Edit Aio_1979016171733291010.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_7

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王016.三图融合-精简_2034657573575598081.json、图片生成/图生图/251223001-分镜一致性11.Qwen三图融合-NF_2003132198746300418.json、图片生成/图生图/251224001.在线版Ps-Qwen-LHSTW30M-三图融合-NF_2003630969938714625.json、图片生成/图生图/LH-DMT版本-2.生图片类-050.Qwen三图融合-NF_2016525076501368833.json、图片生成/图生图/Qwen-Edit 2511 Aio V16单图编辑修改去水印等_2006632675330756610.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 7/11 个有
- `Text Multiline` —— 7/11 个有
- `ImageScaleToTotalPixels` —— 6/11 个有
- `ImageConcanate` —— 4/11 个有
- `CR Prompt Text` —— 3/11 个有
- `DWPreprocessor` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `PDIMAGE_LongerSize` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 11 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler_ancestral | - | 11 | 82% |
| 调度器 | beta | - | 11 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 768 | 720 - 1920 | 11 | 61% |
| 高度 | 768 | 768 - 1280 | 11 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，11 个样本，一致性 82%
- 调度器 最常用 beta，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 720 - 1920，11 个样本
- 高度 中位数 768，观测区间 768 - 1280，11 个样本
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
