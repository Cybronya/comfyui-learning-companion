---
name: text_to_image_lora_sampler_clip_42
type: Text To Image
frequency: 19
level: strong
coverage: 0.877947
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Zen Image Edit写实图像编辑｜图生图修图 其它图片处理一步到位_2104064412368850945.json, 图片生成/图生图/Zen Image Edit图像编辑｜图生图写实修图 其它图片处理全搞定_2104053107750686722.json, 图片生成/图生图/aigc-image-2.5图生图九图模式｜太平风图片批量处理_2106956375321567233.json, 图片生成/图生图/image 2.5图生图_2101659679536537601.json, 图片生成/图生图/image 2.5图生图工作流｜老图翻新重绘｜画质细节双重增强_2101867652611403778.json, 图片生成/图生图/image qwen image 2 1 character sheet with clothes_2108666622264303617.json, 图片生成/图生图/image qwen image 2 1 character sheet1 角色设定图生成_2108668112957698049.json, 图片生成/图生图/image2.5全能编辑器｜图生图修图改图一气呵成｜细节重绘不伤原图_2099110738114736130.json, 图片生成/图生图/qwen2.1漫剧角色三视图，图生图多角度设定一键出_2112290266672619522.json, 图片生成/图生图/qwen2.1漫剧角色三视图｜上传图像即出角色资产三视图｜漫剧创作必备_2112106203827490817.json, 图片生成/图生图/三视图+多表情+多视角Qwen Image 2.1｜角色一致性设计全角度_2114274271144005633.json, 图片生成/图生图/三视图多表情多视角Qwen 2.1｜角色一致性设计专用流_2114040279023046658.json, 图片生成/图生图/三视图多表情多视角Qwen Image 2.1｜角色多角度设计_2114047616643321857.json, 图片生成/图生图/三视图多表情多视角Qwen Image 2.1｜角色设计一致性_2114015336122109953.json, 图片生成/图生图/三视图多表情多视角Qwen工作流｜角色一致性图生图_2114051420059160577.json, 图片生成/图生图/三视图多表情多视角生成 Qwen Image 2.1角色工具_2113680994153881601.json, 图片生成/图生图/三视图多表情多视角生成 Qwen Image 2.1角色工具_2114061571478605826.json, 图片生成/图生图/美少女写实图生图 Qwen Image2.1参考图高质量重绘_2104285634960646145.json, 图片生成/图生图/角色三视图Qwen Image 2.1工作流，图生图角色设计处理工具_2107934196995018753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/Zen Image Edit写实图像编辑｜图生图修图 其它图片处理一步到位_2104064412368850945.json、图片生成/图生图/Zen Image Edit图像编辑｜图生图写实修图 其它图片处理全搞定_2104053107750686722.json、图片生成/图生图/aigc-image-2.5图生图九图模式｜太平风图片批量处理_2106956375321567233.json、图片生成/图生图/image 2.5图生图_2101659679536537601.json、图片生成/图生图/image 2.5图生图工作流｜老图翻新重绘｜画质细节双重增强_2101867652611403778.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 19 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 18/19 个有
- `ResolutionSelector` —— 14/19 个有
- `TextEncodeQwenImage21` —— 13/19 个有
- `ComfySwitchNode` —— 10/19 个有
- `QwenImage21Cache` —— 9/19 个有
- `ImageStitch` —— 8/19 个有
- `PrimitiveFloat` —— 7/19 个有
- `CR Prompt Text` —— 5/19 个有
- `RH_RhartImageG25SunburstImageToImage` —— 4/19 个有
- `Image Comparer (rgthree)` —— 2/19 个有
- `SaveImageAdvanced` —— 2/19 个有
- `ZenImageEditCheckpointLoader` —— 2/19 个有
- `ZenImageEditEncodeAdvanced` —— 2/19 个有
- `easy cleanGpuUsed` —— 2/19 个有
- `ImageScaleToTotalPixels` —— 1/19 个有
- `Text` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（20/19 个样本）：Steps较低可能导致细节不足
