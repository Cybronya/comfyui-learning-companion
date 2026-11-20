---
name: text_to_image_lora_sampler_clip_18
type: Text To Image
frequency: 33
level: strong
coverage: 0.864212
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/6步加速版换头换脸 Qwen Image 2.1高效出图_2104765577515585538.json, 图片生成/图生图/BF16精度Qwen Image 2.1图片编辑，小字不崩的图生图处理方案_2102871104883879938.json, 图片生成/图生图/BF16精度Qwen_Image_2.1图片编辑，小字不崩的图生图处理方案_2105505352971280385.json, 图片生成/图生图/QWEN2.1图像编辑工作流 图片精修局部修改全能处理 图生图必备_2105034860778844162.json, 图片生成/图生图/QWEN2.1图像编辑工作流｜图片精修局部修改全能处理｜图生图必备_2102213493909966850.json, 图片生成/图生图/QWEN2.1图像编辑工作流｜图片精修局部修改全能处理｜图生图必备_2104445483052781569.json, 图片生成/图生图/QWen2.1图像编辑利器｜图生图轻松改图修图一键搞定_2106200271583014914.json, 图片生成/图生图/QWen2.1官方图像编辑工作流，简洁高效的图生图处理方案_2102808314856955905.json, 图片生成/图生图/QWen2.1官方图像编辑工作流，简洁高效的图生图处理方案_2106915667613143041.json, 图片生成/图生图/Qwen Image 2.1一键三视图多表情多视角 角色设定批量产出_2110358998884110338.json, 图片生成/图生图/Qwen Image 2.1三视图多表情多视角 角色设计图生图工具_2113674747845365761.json, 图片生成/图生图/Qwen Image 2.1三视图多表情多视角生成，角色一致性设计一步到位_2114444195971817474.json, 图片生成/图生图/Qwen Image 2.1三视图多表情，多视角分镜出图一站搞定_2110844570106945537.json, 图片生成/图生图/Qwen Image 2.1三视图多表情｜多视角人物设定一键出_2110741200184627201.json, 图片生成/图生图/Qwen Image 2.1去除AI感工作流，写实风格人像图生图自然质感提升_2102839671737896962.json, 图片生成/图生图/Qwen Image 2.1去除AI感文生图图生图处理工具_2102540105742372865.json, 图片生成/图生图/Qwen Image 2.1去除AI感｜美少女写实图秒变真实｜告别塑料质感_2102640016362139650.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102095974146596866.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102100461598892034.json, 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102192876569583617.json, 图片生成/图生图/Qwen Image 2.1换头换脸6步加速版｜图生图换脸又快又稳_2104541964841607170.json, 图片生成/图生图/Qwen Image 2.1精准抠图工作流指哪扣哪交互式图生图体验，图生图抠图工具_2107258835344904194.json, 图片生成/图生图/Qwen Image 2.1自动分镜短剧分镜生成，图生图快速产出故事板_2102850796370096129.json, 图片生成/图生图/Qwen Image 2.1自动分镜短剧分镜生成，图生图快速产出故事板_2103270132993847297.json, 图片生成/图生图/Qwen_Image_2.1去除AI感工作流，写实风格人像图生图自然质感提升_2105864806925430785.json, 图片生成/图生图/三视图+多表情+多视角Qwen Image 2.1｜角色一致性设计全角度_2114274271144005633.json, 图片生成/图生图/三视图多表情多视角Qwen 2.1｜角色一致性设计专用流_2114040279023046658.json, 图片生成/图生图/三视图多表情多视角Qwen Image 2.1｜角色多角度设计_2114047616643321857.json, 图片生成/图生图/三视图多表情多视角Qwen Image 2.1｜角色设计一致性_2114015336122109953.json, 图片生成/图生图/三视图多表情多视角Qwen工作流｜角色一致性图生图_2114051420059160577.json, 图片生成/图生图/三视图多表情多视角生成 Qwen Image 2.1角色工具_2113680994153881601.json, 图片生成/图生图/三视图多表情多视角生成 Qwen Image 2.1角色工具_2114061571478605826.json, 图片生成/文生图/Qwen Image 2.1 角色设定集｜多视图表情姿态全包_2112459574203731970.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 33 个 workflow 归纳得出（图片生成/图生图/6步加速版换头换脸 Qwen Image 2.1高效出图_2104765577515585538.json、图片生成/图生图/BF16精度Qwen Image 2.1图片编辑，小字不崩的图生图处理方案_2102871104883879938.json、图片生成/图生图/BF16精度Qwen_Image_2.1图片编辑，小字不崩的图生图处理方案_2105505352971280385.json、图片生成/图生图/QWEN2.1图像编辑工作流 图片精修局部修改全能处理 图生图必备_2105034860778844162.json、图片生成/图生图/QWEN2.1图像编辑工作流｜图片精修局部修改全能处理｜图生图必备_2102213493909966850.json…）

- **类型**：Text To Image
- **样本数**：33
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 33 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 31/33 个有
- `ResolutionSelector` —— 30/33 个有
- `孤海注释` —— 29/33 个有
- `ImageStitch` —— 17/33 个有
- `PrimitiveFloat` —— 13/33 个有
- `PreviewImage` —— 10/33 个有
- `PrimitiveBoolean` —— 7/33 个有
- `SaveImageAdvanced` —— 7/33 个有
- `EmptyImage` —— 6/33 个有
- `CR Prompt Text` —— 4/33 个有
- `PrimitiveStringMultiline` —— 4/33 个有
- `CR Text` —— 3/33 个有
- `ConcatTextOfUtils` —— 2/33 个有
- `LoraLoaderBypassModelOnly` —— 2/33 个有
- `QwenImage21SageAttentionT8` —— 2/33 个有
- `PrimitiveInt` —— 1/33 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 33 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 33 | 100% |
| 采样算法 | er_sde | - | 33 | 100% |
| 调度器 | beta | - | 33 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 33 | 100% |
| 宽度 | 80 | 80 - 80 | 33 | 100% |
| 高度 | 80 | 80 - 80 | 33 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 38/33 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，33 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，33 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，33 个样本，一致性 100%
- 调度器 最常用 beta，33 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，33 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，33 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，33 个样本，取值集中（一致性 100%）
- 高发问题（38/33 个样本）：Steps较低可能导致细节不足
