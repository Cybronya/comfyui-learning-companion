---
name: text_to_image_lora_sampler_clip_148
type: Text To Image
frequency: 11
level: strong
coverage: 0.905455
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Moss_Image_EDIT图像编辑工作流｜图生图改图不伤原图_2114238030822338562.json, 图片生成/图生图/QWEN PANO360全景图生成工作流 360度全景画面直出_2109702845909000193.json, 图片生成/图生图/Qwen 2.1一键换脸换人，图生图角色替换人物身份无缝对齐_2112241514712756225.json, 图片生成/图生图/Qwen 2.1五视图透明背景，图生图多视角角色设计工具_2103985760100765697.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流，原图姿势参考图一键置换图生图工具_2106172512919965697.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流，参考姿势图生图人体姿态迁移工具_2103979610072506370.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流｜原图姿势参考图一键置换图生图_2103661816684568577.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流｜原图姿势参考图一键置换图生图_2105634379556020226.json, 图片生成/图生图/Qwen Image 2.1一致性保持加图像编辑 角色一致性更强_2109344093791940610.json, 图片生成/图生图/Qwen Image 2.1参考人物姿势，图生图姿势参考生成工具_2103585753916862466.json, 图片生成/图生图/Qwen Image 2.1图像编辑加速版，高效图生图处理工具_2103579830016102401.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_148

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Moss_Image_EDIT图像编辑工作流｜图生图改图不伤原图_2114238030822338562.json、图片生成/图生图/QWEN PANO360全景图生成工作流 360度全景画面直出_2109702845909000193.json、图片生成/图生图/Qwen 2.1一键换脸换人，图生图角色替换人物身份无缝对齐_2112241514712756225.json、图片生成/图生图/Qwen 2.1五视图透明背景，图生图多视角角色设计工具_2103985760100765697.json、图片生成/图生图/Qwen 2.1姿势迁移工作流，原图姿势参考图一键置换图生图工具_2106172512919965697.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 10/11 个有
- `QwenImage21Cache` —— 9/11 个有
- `ResolutionSelector` —— 8/11 个有
- `GetImageSize` —— 6/11 个有
- `easy cleanGpuUsed` —— 6/11 个有
- `AIO_Preprocessor` —— 5/11 个有
- `ComfySwitchNode` —— 3/11 个有
- `CR Prompt Text` —— 2/11 个有
- `QwenPERewriteT8` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `CR Prompt List` —— 1/11 个有
- `FluxKontextImageScale` —— 1/11 个有
- `HAIGC_SaveImagesToZip` —— 1/11 个有
- `Image Comparer (rgthree)` —— 1/11 个有
- `MOSSImageOstrisEditModelPatch` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `SkipLayerGuidanceDiTSimple` —— 1/11 个有
- `TextEncodeMOSSImageOstrisEdit` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
