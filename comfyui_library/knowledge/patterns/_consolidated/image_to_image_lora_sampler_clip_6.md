---
name: image_to_image_lora_sampler_clip_6
type: Image To Image
frequency: 30
level: strong
coverage: 0.856133
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, ImageResizeKJ, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Z-image图生图（洗图工作流）_1994322368636059649.json, 图片生成/图生图/Z-image真实人像质感御姐美女_2040383993207595010.json, 图片生成/图生图/Z-image真实人像质感御姐美女_2040670749035339778.json, 图片生成/图生图/Z-image真实人像质感御姐美女_2040675153893400578.json, 图片生成/图生图/z-image图生图洗图+换脸_2033812036697726978.json, 图片生成/图生图/z-image洗图+换脸_2034819779973877762.json, 图片生成/图生图/东方阳台美女Z-image真实人像质感御姐美女_2040721437132070913.json, 图片生成/图生图/俯视户外Z-image真实人像质感御姐美女_2040702316382261250.json, 图片生成/图生图/古风美女Z-image真实人像质感御姐美女_2040757098669154306.json, 图片生成/图生图/吊带睡衣Z-image真实人像质感御姐美女_2040695666824978433.json, 图片生成/图生图/城市夜景Z-image真实人像质感御姐美女_2040749010746609666.json, 图片生成/图生图/婚纱美女Z-image真实人像质感御姐美女_2040751779763200001.json, 图片生成/图生图/学生妹Z-image真实人像质感御姐美女_2040754502864740354.json, 图片生成/图生图/居家美女Z-image真实人像质感御姐美女_2040768968000016385.json, 图片生成/图生图/巷子印花少女Z-image真实人像质感御姐美女_2040771092754731009.json, 图片生成/图生图/异域风情雪山Z-image真实人像质感御姐美女_2040746277050257410.json, 图片生成/图生图/性感女讲师Z-image真实人像质感御姐美女_2040764424054644738.json, 图片生成/图生图/性感有韵味Z-image真实人像质感御姐美女_2040759701650018306.json, 图片生成/图生图/成熟有气质Z-image真实人像质感御姐美女_2040714815718559746.json, 图片生成/图生图/日常穿搭Z-image真实人像质感御姐美女_2040712721057976321.json, 图片生成/图生图/昏暗灯光Z-image真实人像质感御姐美女_2040743064725098498.json, 图片生成/图生图/晚礼服Z-image真实人像质感御姐美女_2040740478626304001.json, 图片生成/图生图/欧式美女Z-image真实人像质感御姐美女_2040717625264709634.json, 图片生成/图生图/现代客厅美女Z-image真实人像质感御姐美女_2040727682383613954.json, 图片生成/图生图/睡衣吊带Z-image真实人像质感御姐美女_2040706702894436353.json, 图片生成/图生图/短裤Z-image真实人像质感御姐美女_2040681458297217026.json, 图片生成/图生图/立体立绘Z-image真实人像质感御姐美女_2040764633539153921.json, 图片生成/图生图/粉色长发Z-image真实人像质感御姐美女_2040766556665286658.json, 图片生成/图生图/美女写真图Z-image真实人像质感御姐美女_2040709477191655425.json, 图片生成/图生图/蕾丝内衣Z-image真实人像质感御姐美女_2040699285179736066.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/图生图/Z-image图生图（洗图工作流）_1994322368636059649.json、图片生成/图生图/Z-image真实人像质感御姐美女_2040383993207595010.json、图片生成/图生图/Z-image真实人像质感御姐美女_2040670749035339778.json、图片生成/图生图/Z-image真实人像质感御姐美女_2040675153893400578.json、图片生成/图生图/z-image图生图洗图+换脸_2033812036697726978.json…）

- **类型**：Image To Image
- **样本数**：30
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 30 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Note _O` —— 29/30 个有
- `PrimitiveFloat` —— 29/30 个有
- `Qwen3VL_Advanced` —— 29/30 个有
- `easy anythingIndexSwitch` —— 29/30 个有
- `Fast Groups Muter (rgthree)` —— 1/30 个有
- `ImageLoader` —— 1/30 个有
- `ImageStitch` —— 1/30 个有
- `JWStringConcat` —— 1/30 个有
- `Qwen3_VQA` —— 1/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 30 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 30 | 100% |
| 采样算法 | euler | - | 30 | 100% |
| 调度器 | simple | - | 30 | 100% |
| 重绘幅度 | 1 | 0.4 - 1 | 30 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，30 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，30 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，30 个样本，一致性 100%
- 调度器 最常用 simple，30 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，30 个样本，取值集中（一致性 89%）
