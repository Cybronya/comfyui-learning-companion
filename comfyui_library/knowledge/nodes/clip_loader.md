# CLIPLoader

## 节点类型

`CLIPLoader`

## 分类

Model Loading

## 作用

独立加载文本编码器（CLIP / Qwen-VL / T5 类），输出 CLIP 给编码节点。
底模与文本编码器解耦的工作流（Qwen Image 2.1、Flux、H3 等）必备。

## 参数（统计自 404 个真实 workflow，644 次出现）

| 参数 | 说明 | 实测分布 |
|---|---|---|
| clip_name | 编码器文件名 | Qwen 系占多数（qwen_3_06b_base / qwen3vl_8b 等） |
| type | 编码器架构类型 | qwen_image 302 / stable_diffusion 216 / minimax 40 / krea2 37 / flux2 30 / lumina2 13 / wan 5 |
| device | 运行设备 | 99% 为 default；显存不足时可改 cpu |

## 常见问题与风险

- **type 必须与底模族匹配**：Qwen Image 底模配 stable_diffusion 类型
  会导致提示词完全不生效（不是报错，而是画面与提示词无关，最难排查）。
- 同名量化版本（int8_convrot / bf16 / fp8_scaled）显存占用与质量不同，
  低显存优先 int8_convrot。

## 可信度

Generated（2026-10-06，参数分布实测，type 匹配规则为通行语义）TODO(待验证)
