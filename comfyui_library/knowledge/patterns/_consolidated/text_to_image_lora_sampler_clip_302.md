---
name: text_to_image_lora_sampler_clip_302
type: Text To Image
frequency: 6
level: moderate
coverage: 0.944167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWEN 图像旋转万能视角调整_2015957553431187458.json, 图片生成/图生图/Qwen image 人物一致性 多图展示_2044669602428362753.json, 图片生成/图生图/multiple2511 图片多角度、多视角编辑工作流_2013173343419109378.json, 图片生成/图生图/qwen_image_edit_plus_MultipleAngles-运镜+动作-图片多角度编辑_1988568009021284353.json, 图片生成/图生图/图像不同角度  切换角度_2011081053884125185.json, 图片生成/图生图/图像角度控制器-qwen_image_edit_2511_2009827945770127361.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_302

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/QWEN 图像旋转万能视角调整_2015957553431187458.json、图片生成/图生图/Qwen image 人物一致性 多图展示_2044669602428362753.json、图片生成/图生图/multiple2511 图片多角度、多视角编辑工作流_2013173343419109378.json、图片生成/图生图/qwen_image_edit_plus_MultipleAngles-运镜+动作-图片多角度编辑_1988568009021284353.json、图片生成/图生图/图像不同角度  切换角度_2011081053884125185.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
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
- `QwenMultiangleCameraNode` —— 5/6 个有
- `GetImageSize` —— 2/6 个有
- `ImageResize+` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `ConditioningConcat` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 6 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1280 | 856 - 1440 | 6 | 85% |
| 高度 | 720 | 480 - 1920 | 6 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 856 - 1440，6 个样本，取值集中（一致性 85%）
- 高度 中位数 720，观测区间 480 - 1920，6 个样本，取值分散，一致性仅 46%
- 高发问题（15/6 个样本）：Steps较低可能导致细节不足
