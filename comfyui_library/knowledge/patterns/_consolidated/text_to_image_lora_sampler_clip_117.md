---
name: text_to_image_lora_sampler_clip_117
type: Text To Image
frequency: 12
level: strong
coverage: 0.893583
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2.1五视图透明背景，图生图多视角角色设计工具_2103985760100765697.json, 图片生成/图生图/Qwen 2.1动漫转写实工作流，无需触发词图生图动漫风格写实化处理_2105769532047577090.json, 图片生成/图生图/Qwen 2.1图片编辑工作流，简洁高效的图生图处理方案_2103906470701129730.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流，原图姿势参考图一键置换图生图工具_2106172512919965697.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流，参考姿势图生图人体姿态迁移工具_2103979610072506370.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流｜原图姿势参考图一键置换图生图_2103661816684568577.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流｜原图姿势参考图一键置换图生图_2105634379556020226.json, 图片生成/图生图/Qwen Image 2.1一致性保持加图像编辑 角色一致性更强_2109344093791940610.json, 图片生成/图生图/Qwen Image 2.1参考人物姿势，图生图姿势参考生成工具_2103585753916862466.json, 图片生成/图生图/Qwen Image 2.1图像编辑加速版，高效图生图处理工具_2103579830016102401.json, 图片生成/文生图/Qwen 2.1文生图4步加速版｜快节奏出图不影响质量_2103063918653558786.json, 图片生成/文生图/Qwen Image 2.1 PE多宫格生图｜一张出九宫排版素材_2103032143940243457.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_117

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen 2.1五视图透明背景，图生图多视角角色设计工具_2103985760100765697.json、图片生成/图生图/Qwen 2.1动漫转写实工作流，无需触发词图生图动漫风格写实化处理_2105769532047577090.json、图片生成/图生图/Qwen 2.1图片编辑工作流，简洁高效的图生图处理方案_2103906470701129730.json、图片生成/图生图/Qwen 2.1姿势迁移工作流，原图姿势参考图一键置换图生图工具_2106172512919965697.json、图片生成/图生图/Qwen 2.1姿势迁移工作流，参考姿势图生图人体姿态迁移工具_2103979610072506370.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 11/12 个有
- `LoadImage` —— 10/12 个有
- `easy cleanGpuUsed` —— 8/12 个有
- `AIO_Preprocessor` —— 5/12 个有
- `ComfySwitchNode` —— 5/12 个有
- `GetImageSize` —— 5/12 个有
- `CR Prompt Text` —— 4/12 个有
- `QwenPERewriteT8` —— 4/12 个有
- `easy showAnything` —— 4/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `CR Prompt List` —— 1/12 个有
- `HAIGC_SaveImagesToZip` —— 1/12 个有
- `MultiTextConcatenate` —— 1/12 个有
- `PathchSageAttentionKJ` —— 1/12 个有
- `PlaySound|pysssss` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（15/12 个样本）：Steps较低可能导致细节不足
