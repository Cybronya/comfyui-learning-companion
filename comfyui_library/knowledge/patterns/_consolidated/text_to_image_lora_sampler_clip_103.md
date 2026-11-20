---
name: text_to_image_lora_sampler_clip_103
type: Text To Image
frequency: 13
level: strong
coverage: 0.905846
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Moss_Image_EDIT图像编辑工作流｜图生图改图不伤原图_2114238030822338562.json, 图片生成/图生图/QWEN PANO360全景图生成工作流 360度全景画面直出_2109702845909000193.json, 图片生成/图生图/Qwe Image 2.1多维运镜构图变换｜附控制指南图生图_2110742888882724865.json, 图片生成/图生图/Qwen 2.1一键换脸换人，图生图角色替换人物身份无缝对齐_2112241514712756225.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流，原图姿势参考图一键置换图生图工具_2106172512919965697.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流，参考姿势图生图人体姿态迁移工具_2103979610072506370.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流｜原图姿势参考图一键置换图生图_2103661816684568577.json, 图片生成/图生图/Qwen 2.1姿势迁移工作流｜原图姿势参考图一键置换图生图_2105634379556020226.json, 图片生成/图生图/Qwen Image 2.1参考人物姿势，图生图姿势参考生成工具_2103585753916862466.json, 图片生成/图生图/Qwen Image 2.1图像编辑加速版，高效图生图处理工具_2103579830016102401.json, 图片生成/文生图/Qwen 2.1文生图4步加速版｜快节奏出图不影响质量_2103063918653558786.json, 图片生成/文生图/Qwen Image 2.1 PE多宫格生图｜一张出九宫排版素材_2103032143940243457.json, 图片生成/文生图/Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_103

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Moss_Image_EDIT图像编辑工作流｜图生图改图不伤原图_2114238030822338562.json、图片生成/图生图/QWEN PANO360全景图生成工作流 360度全景画面直出_2109702845909000193.json、图片生成/图生图/Qwe Image 2.1多维运镜构图变换｜附控制指南图生图_2110742888882724865.json、图片生成/图生图/Qwen 2.1一键换脸换人，图生图角色替换人物身份无缝对齐_2112241514712756225.json、图片生成/图生图/Qwen 2.1姿势迁移工作流，原图姿势参考图一键置换图生图工具_2106172512919965697.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 12/13 个有
- `QwenImage21Cache` —— 11/13 个有
- `LoadImage` —— 10/13 个有
- `ResolutionSelector` —— 9/13 个有
- `easy cleanGpuUsed` —— 9/13 个有
- `AIO_Preprocessor` —— 5/13 个有
- `CR Prompt Text` —— 5/13 个有
- `ComfySwitchNode` —— 5/13 个有
- `GetImageSize` —— 5/13 个有
- `QwenPERewriteT8` —— 5/13 个有
- `easy showAnything` —— 5/13 个有
- `CR Text` —— 1/13 个有
- `FluxKontextImageScale` —— 1/13 个有
- `MOSSImageOstrisEditModelPatch` —— 1/13 个有
- `PathchSageAttentionKJ` —— 1/13 个有
- `SeedNode` —— 1/13 个有
- `SkipLayerGuidanceDiTSimple` —— 1/13 个有
- `SplitImageWithAlpha` —— 1/13 个有
- `TextEncodeMOSSImageOstrisEdit` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（16/13 个样本）：Steps较低可能导致细节不足
