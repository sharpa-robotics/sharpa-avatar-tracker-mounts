# Sharpa Avatar Tracker Mounts — 中文说明

[English](README.md) · [逐文件下载目录](CATALOG.md) · [坐标定义与矩阵](docs/coordinate-systems.md) · [支持渠道](SUPPORT.md)

这是供 review 的第一版仓库，整理 Sharpa Avatar 手套与外部 tracker / VR 手柄之间的机械转接件和坐标转换资料。资料快照日期为 2026-11-10；已建立 [GitHub 公共仓库](https://github.com/sharpa-robotics/sharpa-avatar-tracker-mounts)。

## 从这里开始 review

1. 看 [下载目录](CATALOG.md)：14 个 STEP 文件，每个文件都有直接相对链接。原始中文文件名与来源映射放在仓库外的本地 review 资料中。
2. 看五个产品说明：[VIVE Tracker](products/vive-tracker/README.md)、[VIVE Ultimate](products/vive-ultimate-tracker/README.md)、[PICO](products/pico-controller/README.md)、[Quest 3 / Touch Plus](products/meta-touch-plus/README.md)、[Touch Pro](products/meta-touch-pro/README.md)。
3. 看 [坐标说明](docs/coordinate-systems.md)：完整列出了来源中的 5 个右手矩阵，说明方向、原点、单位、反变换与位姿组合，并提供 JSON 和可运行例子。
4. 看 [LICENSE](LICENSE) 和 [许可说明](docs/licensing.md)：已经放入 MIT 候选文本，等待确认版权主体和模型适用范围。

## 已知需要确认的地方

| 项目 | 当前处理 |
|---|---|
| Quest 3 行混入 Touch Pro 文件 | 按明确文件名分开；Quest 3 仅纳入明确命名的固定件，未宣称成套适配完成 |
| PICO 具体型号 | 来源只写 PICO，不自行指定 PICO 4 / Neo3 |
| 右手矩阵 | 保留原数值，统一转为米供计算，全部标注未实物验证 |
| 矩阵单位 | VIVE 推导明确使用 mm；其余依据同表及 CAD 单位解释为 mm，仍需标定负责人确认 |
| 左手矩阵 | 未找到明确来源，不通过镜像猜测；左手 CAD 可以下载 |
| Ultimate 安装方向 | 原文指出安装座没有防反插，需确认安装方向与坐标定义 |
| 手套接口版本 | 早期坐标图与当前手册的接口图存在版本对应疑点，需要核对硬件版本 |
| 打印和固定 | 未找到覆盖全部型号的打印、抗松脱和位姿精度验收记录；群内曾反馈魔术贴固定易掉落 |

## 本地验证

在仓库根目录用 Python 3.10+ 执行：

```console
python tools/validate_repository.py
python -m unittest discover -s tests -v
python examples/transform_pose.py --product vive-tracker --point 0 0 0 --allow-unvalidated
```

校验覆盖文件 SHA-256、STEP 文件头尾和毫米单位、矩阵结构与近似旋转性质、文档内部文件链接，以及代码的方向和单位行为。通过这些检查不代表实物或 CAD 几何完成验收。

## 联系与范围

支持邮箱：**[support@sharpa.com](mailto:support@sharpa.com)**。首版包含 tracker / 手柄机械转接件和转换数据，不包含 URDF、机器人模型或实时遥操程序。

群聊记录、个人信息、飞书内部链接、预览水印图和历史未明确型号的两个手柄模型没有作为公开仓库正文纳入。相关 review 依据保存在仓库旁的 review-materials 中。正式验证版发布前的具体工作见 [validation.md](docs/validation.md)。
