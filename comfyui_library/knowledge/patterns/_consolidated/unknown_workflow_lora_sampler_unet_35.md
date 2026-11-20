---
name: unknown_workflow_lora_sampler_unet_35
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.979846
common_nodes: [CLIPLoader, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/71.tonnie-2512基础_2010330338651803650.json, 图片生成/文生图/Qwen Edit 2509未来科技_1990647676465274881.json, 图片生成/文生图/Qwen 手机上的3D广州_2032029277100707841.json, 图片生成/文生图/Qwen 手机上的3D深圳_2032032800974577666.json, 图片生成/文生图/Qwen_Edit_2509古书上的3D插画_1989311154684129281.json, 图片生成/文生图/Qwen_Edit_2509微缩城市鸟瞰_1988774900942909442.json, 图片生成/文生图/Qwen_Edit_2509手机上的3D人物_1989695013087047682.json, 图片生成/文生图/Qwen_Edit_2509手机上的3D城市_1989171870014517249.json, 图片生成/文生图/Qwen_Edit_2509手机上的3D城市_2046760188522274818.json, 图片生成/文生图/Qwen_Edit_2509手机上的3D城市_2082741081346764801.json, 图片生成/文生图/Qwen_Edit_2509胶囊城市_1988927261430648834.json, 图片生成/文生图/Qwen_Edit_3D城市3D微景观_2011800399782617090.json, 图片生成/文生图/wj_image_qwen_Image_2512_2049260894298836994.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_35

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/71.tonnie-2512基础_2010330338651803650.json、图片生成/文生图/Qwen Edit 2509未来科技_1990647676465274881.json、图片生成/文生图/Qwen 手机上的3D广州_2032029277100707841.json、图片生成/文生图/Qwen 手机上的3D深圳_2032032800974577666.json、图片生成/文生图/Qwen_Edit_2509古书上的3D插画_1989311154684129281.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 12/13 个有
- `TextEncodeQwenImageEditPlus` —— 12/13 个有
- `EmptyLatentImage` —— 11/13 个有
- `CLIPTextEncode` —— 2/13 个有
- `EmptySD3LatentImage` —— 2/13 个有
- `PreviewAny` —— 2/13 个有
- `AILab_QwenVL` —— 1/13 个有
- `easy promptLine` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 13 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1024 | 720 - 1280 | 11 | 83% |
| 高度 | 1200 | 720 - 1280 | 11 | 76% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1280，11 个样本，取值集中（一致性 83%）
- 高度 中位数 1200，观测区间 720 - 1280，11 个样本
- 高发问题（12/13 个样本）：Steps较低可能导致细节不足
