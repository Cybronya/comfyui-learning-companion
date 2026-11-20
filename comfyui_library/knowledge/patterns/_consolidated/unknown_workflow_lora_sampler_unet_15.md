---
name: unknown_workflow_lora_sampler_unet_15
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.873478
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader]
problems: []
missing: []
members: ["平台全量/H3 gif 循环视频生成, pika flex LoRA_2117855701690314754.json", 平台全量/H3+PikaFlex_Wallpaper_Loop_动态壁纸_2117863969422667777.json, 平台全量/H3-Pika参考生视频_2117385051943030786.json, 平台全量/H3-Pika参考生视频_2117409188606464001.json, 平台全量/MiniMax H3 × Pika Flex｜Ref2VA 参考图 5秒_2119314016672768002.json, 平台全量/Pika H3 6步 参考生视频_2117504156662583297.json, 平台全量/Pika H3 Flex 多参考图多克隆音频生视频标准版_2118535054195511298.json, 平台全量/Pika H3 Flex 多参考图片生视频标准版_2118213762347003906.json, 平台全量/Pika H3 Flex：参考生视频_2118863445192957954.json, 平台全量/Pika_h3_flex_ref2va_RH发布版_2117446118677241857.json, 平台全量/pika-h3-flex-ref2va_2117249844711608321.json, 数字人/数字人/pika-h3-flex-ref2va_2115987936905875458.json, 视频生成/图生视频/8步加速官流_2108935132144037890.json, 视频生成/图生视频/BUNNY_H3_单采_er_sde_手动Sigma_2109936169202049026.json, 视频生成/图生视频/XD-MinimaxH3-加速版_2111691415095963650.json, 视频生成/图生视频/api竖屏768pH3官流_2110570859592249346.json, 视频生成/图生视频/api竖屏768pH3官流_2111012386319724545.json, 视频生成/图生视频/pika-h3-flex-ref2va_2116042512124170241.json, 视频生成/图生视频/【AI影视剧制作】MiniMaxH3-最优官流_2113081896400936962.json, 视频生成/图生视频/【MINIMAX H3】高动态_单采高清_2109286224707022849.json, 视频生成/图生视频/【阿良绘】MiniMax H3加速版｜速度与质量均衡V2_2109543805493014529.json, 视频生成/图生视频/（2320）H3-最优官流_2089001915131711490.json, 视频生成/文生视频/H3-最优官流_2088982134630469634.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_15

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（平台全量/H3 gif 循环视频生成, pika flex LoRA_2117855701690314754.json、平台全量/H3+PikaFlex_Wallpaper_Loop_动态壁纸_2117863969422667777.json、平台全量/H3-Pika参考生视频_2117385051943030786.json、平台全量/H3-Pika参考生视频_2117409188606464001.json、平台全量/MiniMax H3 × Pika Flex｜Ref2VA 参考图 5秒_2119314016672768002.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 21/23 个有
- `VAEDecodeAudio` —— 21/23 个有
- `CreateVideo` —— 15/23 个有
- `SaveVideo` —— 15/23 个有
- `ModelAttentionBackend` —— 11/23 个有
- `LoadAudio` —— 10/23 个有
- `BlockSparseAttention` —— 9/23 个有
- `ModelPreviewOverrideKJ` —— 9/23 个有
- `VHS_VideoCombine` —— 8/23 个有
- `BasicScheduler` —— 6/23 个有
- `VHS_LoadVideo` —— 6/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/23 个有
- `ComfySwitchNode` —— 3/23 个有
- `PrimitiveBoolean` —— 3/23 个有
- `ImageResizeKJv2` —— 2/23 个有
- `MiniMaxH3Loop` —— 2/23 个有
- `MiniMaxH3LoopDecode` —— 2/23 个有
- `CLIPTextEncode` —— 1/23 个有
- `GetImageSizeAndCount` —— 1/23 个有
- `LoopInterpolate` —— 1/23 个有
- `VHS_LoadAudioUpload` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
